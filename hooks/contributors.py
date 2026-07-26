import os
import re
import logging
import requests

from mkdocs.config import config_options
from mkdocs.structure.pages import Page

from jinja2 import Template
from git import Repo

enabled = os.getenv("CONTRIBUTORS", "0") == "1" or os.getenv("FULL", "0") == "1"
logger = logging.getLogger("mkdocs.hooks.contributors")

TEMPLATE = """

---

<style>
#footer-wrapper {{
    white-space: nowrap;
}}
#footer-wrapper > p {{
    display: flex;
    align-items: center;
    gap: 5px;
    margin-top: -10px;
}}
#footer-wrapper > p > .twemoji > svg {{
    max-width: none;
}}
.contributors {{
    min-width: 30px;
    line-height: 0;
    white-space: normal;
    width: 100%;
}}
.contributors > a {{
    margin-right: -8px;
}}
.contributors > a > img {{
    width: 30px;
    border-radius: 15px;
}}
</style>

<div markdown="1" id="footer-wrapper">

:material-clock-edit-outline: {last_updated}&emsp;&emsp;:simple-github: Contributors {contributors}

</div>
"""

CONTRIBUTORS_TEMPLATE = """
<span class="contributors">
    {% for contributor in contributors %}
        <a href="{{ contributor.url }}" title="{{ contributor.id }}" target="_blank">
            <img src="{{ contributor.avatar }}" alt="{{ contributor.id }}">
        </a>
    {% endfor %}
</span>
"""

if enabled:
    logger.info("hook - contributors is loaded and enabled")
else:
    logger.info("hook - contributors is disabled")

repo = Repo(".")


def on_page_markdown(
    markdown: str, page: Page, config: config_options.Config, files, **kwargs
) -> str:
    if not enabled or page.meta.get("home"):
        return markdown

    src_path = "docs/" + page.file.src_path
    if page.meta.get("grave"):
        old_path = "docs/" + page.meta.get("grave").split("TuringCoursesGrave/")[1]
        if not old_path.endswith("index.md"):
            old_path += "index.md"
    else:
        old_path = None
    last_updated = _get_last_updated(src_path)
    contributors = _get_contributors(src_path, old_path)

    return markdown + TEMPLATE.format(
        last_updated=last_updated, contributors=contributors
    )


def _get_last_updated(path: str) -> str:
    if "general" in path and not path.endswith("index.md"):
        path = "docs/general/data.csv"
    for commit in repo.iter_commits(paths=path):
        return commit.committed_datetime.strftime("%Y-%m-%d")
    return "1970-01-01"


def _get_contributors(path: str, old_path: str | None) -> str:
    contributors = _fetch_contributors_from_github(path, old_path)
    if "general" in path and not path.endswith("index.md"):
        contributors.extend(
            _fetch_contributors_from_github("docs/general/data.csv", None)
        )
        contributors = _distinct(contributors)
    raw = Template(CONTRIBUTORS_TEMPLATE).render(contributors=contributors)
    return re.sub(r"(\n| {2,})", "", raw).strip()


def _fetch_contributors_from_github(path: str, old_path: str | None) -> list:
    contributors = []
    if old_path is not None:
        fetch_url = f"https://github.com/ZJU-Turing/TuringCourses/contributors-list/v1.0.0/{old_path}"
        contributors.extend(_fetch_contributors_from_url(fetch_url))
    fetch_url = (
        f"https://github.com/ZJU-Turing/TuringCourses/contributors-list/master/{path}"
    )
    contributors.extend(_fetch_contributors_from_url(fetch_url))
    return _distinct(contributors)


def _fetch_contributors_from_url(fetch_url: str) -> list:
    contributors = []
    try:
        res = requests.get(fetch_url)
        res.raise_for_status()
    except requests.exceptions.HTTPError as err:
        logger.warning(f"Failed to fetch contributors list from {fetch_url}: {err}")
    except Exception as err:
        logger.warning(f"Exception occurred when fetching {fetch_url}: {err}")
    else:
        content = res.text
        re_results = re.findall(
            r"<a.*?href=\"/(?P<id>.*?)\".*?src=\"(?P<avatar>.*?)\"", content, re.DOTALL
        )
        for result in re_results:
            contributors.append(
                {
                    "id": result[0],
                    "avatar": result[1].split("?")[0],
                    "url": f"https://github.com/{result[0]}",
                }
            )
    return contributors


def _distinct(contributors: list) -> list:
    ret = []
    for contributor in contributors:
        if contributor["id"] not in map(lambda x: x["id"], ret):
            ret.append(contributor)
    return ret
