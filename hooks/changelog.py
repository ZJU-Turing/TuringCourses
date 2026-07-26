import os
import re
import logging
import datetime

from mkdocs.config import config_options
from mkdocs.structure.pages import Page
from mkdocs.utils.meta import get_data

from git import Repo, Commit

enabled = os.getenv("CHANGELOG", "0") == "1" or os.getenv("FULL", "0") == "1"
logger = logging.getLogger("mkdocs.hooks.changelog")

template = """- <span style="font-family: var(--md-code-font-family)">{time} [{commit_sha}]({commit_url}) </span>{commit_message}{links}"""

if enabled:
    logger.info("hook - changelog is loaded and enabled")
else:
    logger.info("hook - changelog is disabled")

repo = Repo(".")


def on_page_markdown(
    markdown: str, page: Page, config: config_options.Config, files, **kwargs
) -> str:
    if not enabled or not page.meta.get("changelog"):
        return markdown
    changelogs = _get_changelog_items(page)
    return markdown.replace("{{ changelog }}", changelogs)


def _get_changelog_items(page: Page):
    res = ""
    year = 1970
    checkouted = False
    now_commit = repo.head.commit
    for commit in list(repo.iter_commits()):
        if not checkouted and _before_grave(commit):
            repo.git.checkout("v1.0.1")
            checkouted = True
        now_year = commit.committed_datetime.year
        if now_year != year:
            year = now_year
            res += f"\n## {year} 年\n"
        commit_sha = commit.hexsha[:7]
        commit_url = (
            f"https://github.com/ZJU-Turing/TuringCourses/commit/{commit.hexsha}"
        )
        message = commit.summary
        if (
            message.startswith("Merge pull request")
            or "[skip changelog]" in commit.message
        ):
            continue
        commit_message = re.sub(
            r"#(\d+)",
            r"[#\1](https://github.com/ZJU-Turing/TuringCourses/pull/\1)",
            message,
        )
        time = commit.committed_datetime.strftime("%m-%d")

        changed_filenames = commit.stats.files.keys()
        docs_filenames = [
            filename
            for filename in changed_filenames
            if filename.startswith("docs/")
            and filename.endswith(".md")
            and filename.count("/") == 3
            and os.path.exists(filename)
        ]
        links = ""
        extra_count = 0
        for doc_path in docs_filenames:
            title = _get_title(doc_path).strip()
            if title in ["专业必修课", "专业选修课"]:
                continue
            if _before_grave(commit):
                doc_url = doc_path.replace(
                    "docs/", "https://zju-turing.github.io/TuringCoursesGrave/"
                ).replace("index.md", "")
            else:
                doc_url = doc_path.replace(
                    "docs/", "https://zju-turing.github.io/TuringCourses/"
                ).replace("index.md", "")

            search_strs = [title]
            _, meta = get_data(open(doc_path, "r", encoding="utf-8").read())
            if meta.get("abbrs"):
                search_strs += meta.get("abbrs")
            for abbr in search_strs[::]:
                if abbr.encode("utf-8").isalpha():
                    search_strs.append(abbr.upper())

            for search_str in search_strs:  # need a smarter algorithm
                if search_str in commit_message:
                    if f"[{search_str}" in commit_message:
                        continue
                    commit_message = commit_message.replace(
                        search_str, f"[{search_str}]({doc_url})"
                    )
                    break
            else:
                if extra_count == 4:
                    links += "..."
                    extra_count += 1
                    continue
                elif extra_count == 5:
                    continue
                links += f"[{title}]({doc_url}) "
                extra_count += 1

        if links:
            links = "\n    - 🔗 " + links

        res += (
            template.format(
                commit_sha=commit_sha,
                commit_url=commit_url,
                commit_message=commit_message,
                links=links,
                time=time,
            )
            + "\n"
        )

    repo.git.checkout(now_commit.hexsha)
    return res


def _before_grave(commit: Commit) -> bool:
    return commit.committed_datetime < datetime.datetime(
        2025, 7, 20, 0, 0, 0, tzinfo=datetime.timezone.utc
    )


def _get_title_from_content(markdown: str) -> str:
    return re.search(r"^# (.*)", markdown, re.M).group(1)


def _get_title(path: str) -> str:
    return _get_title_from_content(open(path, "r", encoding="utf-8").read())
