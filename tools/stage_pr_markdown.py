#!/usr/bin/env python3
"""Stage Markdown from a pull request without checking out its code.

This program runs only from the trusted default branch in a
``pull_request_target`` workflow. It retrieves Markdown as data using the
GitHub API, then overlays it onto that default-branch revision for linters.
It must not be changed to fetch the pull request's repository or to execute
its files.
"""

from __future__ import annotations

import json
import os
import re
import sys
from pathlib import Path, PurePosixPath
from typing import Any, NoReturn
from urllib.error import HTTPError, URLError
from urllib.parse import quote
from urllib.request import Request, urlopen


SAFE_MARKDOWN_PATH = re.compile(r"[\w./-]+\.md\Z", re.UNICODE)
MAX_PR_FILE_PAGES = 30  # GitHub returns at most 100 files per page.


def fail(message: str) -> NoReturn:
    raise RuntimeError(message)


def api_request(url: str, token: str, *, accept: str) -> bytes:
    request = Request(
        url,
        headers={
            "Accept": accept,
            "Authorization": f"Bearer {token}",
            "User-Agent": "turingcourses-autoreview",
            "X-GitHub-Api-Version": "2022-11-28",
        },
    )
    try:
        with urlopen(request, timeout=30) as response:
            return response.read()
    except HTTPError as error:
        fail(f"GitHub API request failed with HTTP {error.code}.")
    except URLError as error:
        fail(f"GitHub API request failed: {error.reason}.")


def api_json(url: str, token: str) -> Any:
    try:
        return json.loads(api_request(url, token, accept="application/vnd.github+json"))
    except json.JSONDecodeError:
        fail("GitHub API returned invalid JSON.")


def validated_path(filename: str) -> tuple[str, ...]:
    """Return a shell-safe, workspace-relative Markdown path or fail closed."""
    if not SAFE_MARKDOWN_PATH.fullmatch(filename):
        fail(f"Refusing an unsafe Markdown path: {filename!r}.")

    path = PurePosixPath(filename)
    if path.is_absolute() or any(part in {"", ".", ".."} or part.startswith("-") for part in path.parts):
        fail(f"Refusing an unsafe Markdown path: {filename!r}.")
    return path.parts


def destination(workspace: Path, parts: tuple[str, ...]) -> Path:
    """Create only real directories below workspace and return a safe target."""
    current = workspace
    for part in parts[:-1]:
        current /= part
        if current.is_symlink():
            fail(f"Refusing to write through symlinked directory: {current.relative_to(workspace)}.")
        if current.exists():
            if not current.is_dir():
                fail(f"Expected a directory at: {current.relative_to(workspace)}.")
        else:
            current.mkdir()

    target = current / parts[-1]
    if target.is_symlink() or target.is_dir():
        fail(f"Refusing to replace a non-regular file: {target.relative_to(workspace)}.")
    return target


def write_outputs(has_markdown: bool, files: list[str]) -> None:
    output_path = os.environ.get("GITHUB_OUTPUT")
    if not output_path:
        fail("GITHUB_OUTPUT is not set.")

    # Each path has passed validated_path: no whitespace, shell metacharacters,
    # newlines, or option-like components can reach later action inputs.
    with Path(output_path).open("a", encoding="utf-8") as output:
        output.write(f"has_markdown={'true' if has_markdown else 'false'}\n")
        output.write(f"markdownlint_files={' '.join(files)}\n")


def main() -> None:
    token = os.environ.get("GITHUB_TOKEN")
    repository = os.environ.get("GITHUB_REPOSITORY")
    api_url = os.environ.get("GITHUB_API_URL", "https://api.github.com").rstrip("/")
    workspace_value = os.environ.get("GITHUB_WORKSPACE")
    pr_number_value = os.environ.get("PR_NUMBER")
    if not all((token, repository, workspace_value, pr_number_value)):
        fail("GITHUB_TOKEN, GITHUB_REPOSITORY, GITHUB_WORKSPACE, and PR_NUMBER are required.")

    try:
        pr_number = int(pr_number_value)
    except ValueError:
        fail("PR_NUMBER is invalid.")
    if pr_number <= 0:
        fail("PR_NUMBER is invalid.")

    workspace = Path(workspace_value).resolve()
    repo_path = quote(repository, safe="/")
    pull_url = f"{api_url}/repos/{repo_path}/pulls/{pr_number}"
    pull = api_json(pull_url, token)
    try:
        head_repo = pull["head"]["repo"]["full_name"]
        head_sha = pull["head"]["sha"]
    except (KeyError, TypeError):
        fail("Pull request head repository or SHA is unavailable.")
    if not isinstance(head_repo, str) or not re.fullmatch(r"[\w.-]+/[\w.-]+", head_repo):
        fail("Pull request head repository is invalid.")
    if not isinstance(head_sha, str) or not re.fullmatch(r"[0-9a-f]{40,64}", head_sha):
        fail("Pull request head SHA is invalid.")

    changed_files: list[dict[str, Any]] = []
    for page in range(1, MAX_PR_FILE_PAGES + 1):
        page_url = f"{pull_url}/files?per_page=100&page={page}"
        page_files = api_json(page_url, token)
        if not isinstance(page_files, list):
            fail("GitHub API returned an invalid pull request file list.")
        changed_files.extend(page_files)
        if len(page_files) < 100:
            break
    else:
        fail("Pull request has too many changed files to review safely.")

    staged_files: list[str] = []
    for changed_file in changed_files:
        if not isinstance(changed_file, dict):
            fail("GitHub API returned an invalid changed-file entry.")
        filename = changed_file.get("filename")
        status = changed_file.get("status")
        if not isinstance(filename, str) or not filename.endswith(".md"):
            continue
        if not isinstance(status, str):
            fail("GitHub API returned an invalid changed-file status.")

        parts = validated_path(filename)
        target = destination(workspace, parts)
        if status == "removed":
            if target.exists():
                target.unlink()
            continue

        contents_url = (
            f"{api_url}/repos/{quote(head_repo, safe='/')}/contents/"
            f"{quote(filename, safe='/')}?ref={quote(head_sha, safe='')}"
        )
        contents = api_request(contents_url, token, accept="application/vnd.github.raw+json")
        target.write_bytes(contents)
        staged_files.append(filename)

    staged_files.sort()
    write_outputs(bool(staged_files), staged_files)
    print(f"Staged {len(staged_files)} Markdown file(s) from pull request #{pr_number}.")


if __name__ == "__main__":
    try:
        main()
    except RuntimeError as error:
        print(f"::error::{error}", file=sys.stderr)
        sys.exit(1)
