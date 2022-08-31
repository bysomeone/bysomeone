"""
@Acknowledgement: This script and the whole workflow are
inspired by the awesome work at https://github.com/tw93/tw93
"""
import requests
import re
from pathlib import Path


CODE_TIME = "https://gist.githubusercontent.com/Whisker17/614c9ba7c639b6097e9d4a689dd8e0f9/raw/8c5f6c896addf47f2cadc23f3353d39a167756a9/waka"
root = Path(__file__).parent.resolve()
README = root / "README.md"


def replace_text(text, replacement, identifier) -> str:
    r = re.compile(
        fr"<!\-\- {identifier} starts \-\->.*<!\-\- {identifier} ends \-\->", re.DOTALL
    )
    replacement = f"<!-- {identifier} starts -->\n{replacement}\n<!-- {identifier} ends -->"
    return r.sub(replacement, text)


def fetch_code_time() -> requests.Response:
    return requests.get(CODE_TIME)


def main():
    # read in self
    md = README.open("r").read()

    # watch out for side effects
    code_time_text = f"\n```text\n{fetch_code_time().text}\n```\n"
    md = replace_text(md, code_time_text, "code_time")

    # write back the updated contents to self
    README.open("w").write(md)

if __name__ == "__main__":
    main()