import os
import time
import logging

from mkdocs.config import config_options
from mkdocs.structure.pages import Page

from git import Repo

enabled = os.getenv("OUTDATE", "0") == "1" or os.getenv("FULL", "0") == "1"
logger = logging.getLogger("mkdocs.hooks.outdate")

# settings
month = 12
exclude = [
    "index.md",
    "template.md",
    "changelog.md",
    "contributing.md",
    "general/index.md",
    "short_term/index.md",
    "political/index.md",
    "others/index.md",
    "math_phys/index.md",
    "readings/index.md",
    "major/mandatory/index.md",
    "major/elective/index.md",
]
exclude_todo = True

CSS_INJECTION = """
<style>
.md-content .admonition:first-of-type {
    display: none;
    margin-top: 0;
}
</style>
""".strip()

JS_INJECTION = """
<script>
(() => {
    let banner = document.querySelector(".md-content .admonition:first-of-type");
    let child = banner.children[0];
    let time_updated = new Date(child.innerText * 1000);
    let time_current = new Date();
    let diff_month = (time_current - time_updated) / 1000 / 60 / 60 / 24 / 30;
    if (diff_month > %f) {
        banner.style.display = "flow-root";
        child.innerHTML = "本页面最后更新于 " + Math.round(diff_month) + " 个月前，内容可能已经过时，请注意鉴别";
    }
})();
</script>
""".strip()

if enabled:
    logger.info("hook - outdate warning is loaded and enabled")
else:
    logger.info("hook - outdate warning is disabled")

repo = Repo(".")


def on_page_markdown(
    markdown: str, page: Page, config: config_options.Config, files, **kwargs
) -> str:
    if not enabled or page.meta.get("ignore_outdate"):
        return markdown
    for file in exclude:
        if page.file.src_uri == file:
            return markdown
    if exclude_todo:
        if "#TODO" in markdown:
            return markdown

    file_path = page.file.abs_src_path
    if "general" in page.file.src_uri:
        file_path = "docs/general/data.csv"
    page_timestamp = _get_latest_commit_timestamp(file_path)
    diff_month = month

    return '!!! warning "%s"\n\n\n%s\n%s%s' % (
        page_timestamp,
        markdown,
        CSS_INJECTION,
        JS_INJECTION % diff_month,
    )


def _get_latest_commit_timestamp(path: str) -> int:
    realpath = os.path.realpath(path)
    commit_timestamp = repo.git.log(realpath, format="%at", n=1)
    if commit_timestamp == "":
        commit_timestamp = time.time()
    return int(commit_timestamp)
