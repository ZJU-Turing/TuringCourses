import os
import re
import sys

CJK = "\u2e80-\u2eff\u2f00-\u2fdf\u3040-\u309f\u30a0-\u30fa\u30fc-\u30ff\u3100-\u312f\u3200-\u32ff\u3400-\u4dbf\u4e00-\u9fff\uf900-\ufaff"
A = "A-Za-z\u0080-\u00ff\u0370-\u03ff"
N = "0-9"
S = "`~!@#\\$%\\^&\\*\\(\\)-_=\\+\\[\\]{}\\\\\\|;:'\",<.>\\/\\?"
EN_BD = ",.;:?!"
BD = r"。．，、：；！‼？⁇·・‧「『（《〈【〖〔［｛」』）》〉】〗〕］｝"

RULES = [
    ("WARNING", "出现制表符", r"\t"),
    ("ERROR", "中文字符间出现空格", rf"[{CJK}] +[{CJK}]"),
    # ("ERROR", "中英字符后接标点间出现空格", rf"[{A}{N}{CJK}] +[{EN_BD}{BD}]"),
    ("ERROR", "英文字符后接标点间出现空格", rf"[{A}{N}] +[{EN_BD}{BD}]"),
    # ("ERROR", "中文字符后接英文标点", rf"[{CJK}][{EN_BD}]"),
    ("ERROR", "英文标点后接中文字符", rf"[{EN_BD}][{CJK}]"),
    # ("ERROR", "中文标点后接空格", rf"[{BD}] "),
]

EXCLUDE = ["./docs/major/introduction_to_data_visualization/数据可视化导论小测.md"]


class ResultLogger:
    def __init__(self):
        self.results = []

    def log(self, level: str, message: str, path: str, line_no: int):
        self.results.append((level, message, path, line_no + 1))

    def info(self, message: str, path: str, line_no: int):
        self.log("INFO", message, path, line_no)

    def warn(self, message: str, path: str, line_no: int):
        self.log("WARNING", message, path, line_no)

    def error(self, message: str, path: str, line_no: int):
        self.log("ERROR", message, path, line_no)

    def export_result_ci(self):
        for level, msg, path, line_no in self.results:
            print(f"{path}:{line_no}:{level[0].lower()} {msg}")

    def export_result_console(self):
        if self.results:
            print("标点符号使用情况检查结果（可能存在误判，请人工甄别）：\n")
            print("|等级|问题原因|文件路径|行号|")
            print("|:--:|:--|:--|:--:|")
            for level, msg, path, line_no in self.results:
                print(f"|{level}|{msg}|{path}|{line_no}|")
        else:
            print("未发现标点符号相关问题 :)")

    def export_result_rich(self):
        from rich.text import Text
        from rich.table import Table
        from rich.console import Console

        console = Console()
        for level, msg, path, line_no in self.results:
            output = Table.grid(padding=(0, 1))
            output.expand = True
            output.add_column(style="log.level", width=None)
            output.add_column(ratio=1, style="log.message", no_wrap=False)
            output.add_column(style="log.path")
            row = []
            row.append(Text.styled(level.ljust(8), f"logging.level.{level.lower()}"))
            row.append(Text(msg))
            row.append(Text(f"{path}:{line_no}"))
            output.add_row(*row)
            console.print(output)


class PunctuationChecker:
    def __init__(self, path: str, logger: ResultLogger):
        self.path = path
        self.logger = logger
        with open(path, "r", encoding="utf-8") as file:
            self.content = file.read()
        self.content = self.pure_text(self.content)
        self.check_punctuation()

    def pure_text(self, text: str) -> str:
        text = re.sub(r":([^ ]+):", r"\1", text)  # remove emoji
        text = re.sub(r"!\[[^\]]*\]\([^)]*\)", "", text)  # remove images
        text = re.sub(r"\[([^\]]*)\]\([^)]*\)", r"\1", text)  # replace links with text
        text = re.sub(r"<!--.*?-->", "", text)  # remove single line comments
        text = re.sub(r"\{#.*?\}", "", text)  # remove class tags
        text = re.sub(r"<a[^>]*>(.*?)</a>", r"\1", text)  # replace HTML links with text
        return text

    def check_parentheses(self, line: str, idx: int):
        in_en, in_cn, error_cn_in_en = False, False, False
        for char in line:
            if in_en and re.match(rf"[{CJK}]", char) and not error_cn_in_en:
                self.logger.error("英文括号内出现中文字符", self.path, idx)
                error_cn_in_en = True
            if char == "(":
                if in_en or in_cn:
                    self.logger.warn("存在括号嵌套，请手动检查", self.path, idx)
                    return
                in_en = True
            elif char == ")":
                if not in_en:
                    self.logger.error("出现未配对的英文右括号", self.path, idx)
                in_en = False
            elif char == "（":
                if in_en or in_cn:
                    self.logger.warn("存在括号嵌套，请手动检查", self.path, idx)
                    return
                in_cn = True
            elif char == "）":
                if not in_cn:
                    self.logger.error("出现未配对的中文右括号", self.path, idx)
                in_cn = False
        if in_en:
            self.logger.error("出现未配对的英文左括号", self.path, idx)
        if in_cn:
            self.logger.warn("出现未配对的中文左括号（", self.path, idx)

    def check_punctuation(self):
        in_comment = False
        for idx, line in enumerate(self.content.splitlines()):
            if line.strip() == "" or in_comment:
                continue

            if "<!--" in line:  # has made sure it's multi-line
                in_comment = True
                line = line.split("<!--")[0]
            elif "-->" in line and in_comment:
                in_comment = False
                line = line.split("-->")[-1]

            for level, msg, pattern in RULES:
                if re.search(pattern, line.strip(" ")):
                    self.logger.log(level, msg, self.path, idx)

            self.check_parentheses(line, idx)


if __name__ == "__main__":
    logger = ResultLogger()
    if len(sys.argv) == 2:
        files = sys.argv[1].split()
        for file_path in files:
            if not os.path.exists(file_path):
                logger.info("文件已被删除", file_path, 0)
                continue
            PunctuationChecker(file_path, logger)
        logger.export_result_ci()
    else:
        for root, dirs, files in os.walk("."):
            for file in files:
                if file.endswith(".md"):
                    file_path = os.path.join(root, file)
                    if file_path in EXCLUDE:
                        continue
                    PunctuationChecker(file_path, logger)
        logger.export_result_rich()
