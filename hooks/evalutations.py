import os
import csv
import logging

from mkdocs.config import config_options
from mkdocs.structure.pages import Page

enabled = os.getenv("EVALUATIONS", "1") == "1" or os.getenv("FULL", "0") == "1"
logger = logging.getLogger("mkdocs.hooks.evaluations")

art_tag = "![](https://img.shields.io/badge/-美育认定-blue?style=flat-square)"
lab_tag = "![](https://img.shields.io/badge/-劳育认定-brown?style=flat-square)"
template = """
???+ general "*{score}* | {name}"
{content}
""".strip()

if enabled:
    logger.info("hook - evaluations is loaded and enabled")
else:
    logger.info("hook - evaluations is disabled")

with open("docs/general/data.csv", "r", encoding="UTF-8") as f:
    csv_reader = csv.DictReader(f)
    all_items = list(csv_reader)
    all_items.sort(key=lambda x: int(x["年级"]), reverse=True)


def on_page_markdown(
    markdown: str, page: Page, config: config_options.Config, files, **kwargs
) -> str:
    if not enabled or not page.meta.get("evaluations"):
        return markdown
    return markdown.replace(
        "{{ evaluations }}", _get_page_markdown(page.meta.get("evaluations").strip())
    )


def _get_page_markdown(class_name: str) -> str:
    markdown = ""
    items = list(filter(lambda x: x["课程大类"] == class_name, all_items))
    cat_list = list(map(lambda x: x["具体分类"], items))
    cat_set = sorted(set(cat_list), key=cat_list.index)
    for cat in cat_set:
        markdown += f"## {cat}\n\n"
        cat_items = list(filter(lambda x: x["具体分类"] == cat, items))
        course_list = list(map(lambda x: x["课程名称"], cat_items))
        course_set = sorted(set(course_list), key=course_list.index)
        for course in course_set:
            course_items = list(filter(lambda x: x["课程名称"] == course, cat_items))
            grades_set = set(map(lambda x: int(x["年级"]), course_items))
            if course_items[0]["美育认定"] == "True":
                markdown += f"### {course} {art_tag}\n\n"
            elif course_items[0]["劳育认定"] == "True":
                markdown += f"### {course} {lab_tag}\n\n"
            else:
                markdown += f"### {course}\n\n"
            for grade in list(grades_set)[::-1]:
                markdown += f'=== "{grade} 级"\n'
                grade_items = list(
                    filter(lambda x: int(x["年级"]) == grade, course_items)
                )
                for item in grade_items:
                    formated = template.format(
                        score=item["评分"],
                        name=item["姓名"] if item["姓名"].strip() else "匿名",
                        content=_indent(item["评价"]),
                    )
                    markdown += _indent(formated) + "\n"
            markdown += "\n"
    return markdown


def _indent(text: str, amount: int = 4) -> str:
    return "\n".join(" " * amount + line for line in text.splitlines())
