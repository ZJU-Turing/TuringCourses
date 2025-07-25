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

abbrs = { # for backward compatibility
    "嵌入式系统": ["嵌入式"],
    "计算机体系结构": ["体系结构"],
    "操作系统原理与实践": ["os"],
    "数学分析（甲）Ⅱ（H）": ["数分Ⅱ", "数分II", "数分 II", "数分二", "数分"],
    "数学分析（甲）Ⅰ（H）": ["数分Ⅰ", "数分I", "数分 I", "数分一", "数分", "数学分析（甲）I（H）"],
    "概率论（H）": ["概率论"],
    "算法竞赛集训（ACM）": ["ACM 短学期"],
    "高级数据结构与算法分析": ["ads"],
    "数据结构基础": ["fds"],
    "面向对象程序设计": ["oop"],
    "离散数学理论基础": ["离散"],
    "线性代数 Ⅰ（H）": ["线性代数 I（H）", "线代I", "线代Ⅰ", "线代一", "线代"],
    "线性代数 Ⅱ（H）": ["线性代数 II（H）", "线代II", "线代Ⅱ", "线代二", "线代"],
    "常微分方程": ["ode"],
    "普通物理学 Ⅱ（H）": ["普通物理学Ⅱ（H）", "普物 Ⅱ", "普物II"],
    "普通物理学 Ⅰ（H）": ["普通物理学Ⅰ（H）", "普物 Ⅰ", "普物I"],
    "普通物理学实验 Ⅰ": ["普物实验Ⅰ", "普物实验I", "普物实验"],
    "优化基本理论与方法": ["凸优化"],
    "超算实训（HPC）": ["超算"],
    "数据要素市场概论": ["数据要素市场"],
    "计算机组成与设计": ["计组"],
    "理论计算机科学导引": ["计算理论", "toc"],
    "安全攻防实践（CTF）": ["AAA 短学期"],
    "计算机系统 Ⅰ": ["计算机系统 I", "计算机系统Ⅰ"],
    "计算机系统 Ⅱ": ["计算机系统 II", "计算机系统Ⅱ"],
    "计算机系统 Ⅲ": ["计算机系统 III", "计算机系统Ⅲ"],
    "人工智能基础/引论": ["人工智能基础"],
    "编译原理": ["compiler"],
    "机器学习": ["ml"],
    "数据安全与隐私保护": ["数据安全"],
    "软件安全原理和实践": ["软件安全"],
    "毛泽东思想与中国特色社会主义理论体系概论（H）": ["毛概"],
    "习近平新时代中国特色社会主义思想概论": ["习概"],
    "形势与政策 Ⅰ": ["形策Ⅰ", "形策I"],
    "人工智能伦理与安全": ["AI 伦理"],
}

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
    for commit in repo.iter_commits():
        if (not checkouted and _before_grave(commit)):
            repo.git.checkout('v1.0.0')
            checkouted = True
        now_year = commit.committed_datetime.year
        if now_year != year:
            year = now_year
            res += f"\n## {year} 年\n"
        commit_sha = commit.hexsha[:7]
        commit_url = f"https://github.com/ZJU-Turing/TuringCourses/commit/{commit.hexsha}"
        message = commit.summary
        if (message.startswith("Merge pull request") or "[skip changelog]" in commit.message):
            continue
        commit_message = re.sub(r"#(\d+)", r"[#\1](https://github.com/ZJU-Turing/TuringCourses/pull/\1)", message)
        time = commit.committed_datetime.strftime("%m-%d")

        changed_filenames = commit.stats.files.keys()
        docs_filenames = [
            filename for filename in changed_filenames 
                if filename.startswith("docs/") and 
                    filename.endswith(".md") and 
                    filename.count("/") == 3 and
                    os.path.exists(filename)
        ]
        links = ""
        extra_count = 0
        for doc_path in docs_filenames:
            title = _get_title(doc_path).strip()
            if title in ["专业必修课", "专业选修课"]:
                continue
            if _before_grave(commit):
                doc_url = doc_path.replace("docs/", "https://zju-turing.github.io/TuringCoursesGrave/").replace("index.md", "")
            else:
                doc_url = doc_path.replace("docs/", "https://zju-turing.github.io/TuringCourses/").replace("index.md", "")

            search_strs = [title]
            for abbr in abbrs.get(title, []):
                search_strs.append(abbr)
                if abbr.encode("utf-8").isalpha():
                    search_strs.append(abbr.upper())
            _, meta = get_data(open(doc_path, "r", encoding="utf-8").read())
            if meta.get("abbrs"):
                search_strs += meta.get("abbrs")

            for search_str in search_strs: # need a smarter algorithm
                if search_str in commit_message:
                    if f"[{search_str}" in commit_message:
                        continue
                    commit_message = commit_message.replace(search_str, f"[{search_str}]({doc_url})")
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
        
        res += template.format(commit_sha=commit_sha, commit_url=commit_url, commit_message=commit_message, links=links, time=time) + "\n"
    
    repo.git.checkout(now_commit.hexsha)
    return res

def _before_grave(commit: Commit) -> bool:
    return commit.committed_datetime < datetime.datetime(2025, 7, 20, 0, 0, 0, tzinfo=datetime.timezone.utc)

def _get_title_from_content(markdown: str) -> str:
    return re.search(r"^# (.*)", markdown, re.M).group(1)

def _get_title(path: str) -> str:
    return _get_title_from_content(open(path, "r", encoding="utf-8").read())
