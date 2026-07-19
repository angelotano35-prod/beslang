"""
Add these files to your existing beslang-v4 project to make it pip-installable
with a real 'beslang' command. Run this script inside your beslang-v4 folder.

Usage:
    python setup_cli_package.py
"""

import os

PACKAGE_NAME = "beslang-lang"  # the name people will `pip install`
COMMAND_NAME = "beslang"        # the command they'll type once installed
YOUR_NAME = "Angelo Tano"
YOUR_EMAIL = "angelotano35@gmail.com"

files = {
    "beslang/cli.py": '''import sys
import argparse
from .lexer import tokenize
from .parser import Parser
from .interpreter import Interpreter, BesLangError


def run_file(filepath, show_tokens=False):
    with open(filepath, "r", encoding="utf-8") as f:
        source = f.read()

    try:
        tokens = tokenize(source)
        if show_tokens:
            print("--- Tokens ---")
            for tok in tokens:
                print(tok)
            print("--- Output ---")

        parser = Parser(tokens)
        statements = parser.parse_program()
        interpreter = Interpreter()
        interpreter.run(statements)
    except BesLangError as e:
        print(f"\\nOops! {e}")
        sys.exit(1)
    except SyntaxError as e:
        print(f"\\nOops! {e}")
        sys.exit(1)


def main():
    parser = argparse.ArgumentParser(
        prog="beslang",
        description="Run a BesLang (.bes) program - a Filipino-flavored toy programming language."
    )
    parser.add_argument("file", help="Path to a .bes file to run")
    parser.add_argument(
        "--show-tokens", action="store_true",
        help="Print the token stream before running (useful for debugging)"
    )
    parser.add_argument(
        "--version", action="version", version="BesLang 0.1.0"
    )

    args = parser.parse_args()
    run_file(args.file, show_tokens=args.show_tokens)


if __name__ == "__main__":
    main()
''',

    "pyproject.toml": f'''[build-system]
requires = ["setuptools>=61.0"]
build-backend = "setuptools.build_meta"

[project]
name = "{PACKAGE_NAME}"
version = "0.1.0"
description = "BesLang: a toy programming language using Filipino Gen Z slang, with its own lexer, parser, and interpreter"
readme = "README.md"
requires-python = ">=3.9"
license = {{text = "MIT"}}
authors = [
    {{name = "{YOUR_NAME}", email = "{YOUR_EMAIL}"}}
]
classifiers = [
    "Programming Language :: Python :: 3",
    "License :: OSI Approved :: MIT License",
    "Operating System :: OS Independent",
    "Topic :: Software Development :: Interpreters",
]

[project.scripts]
{COMMAND_NAME} = "beslang.cli:main"

[project.urls]
Homepage = "https://github.com/angelotano35-prod/beslang"
''',

    "LICENSE": '''MIT License

Copyright (c) 2026 Angelo Tano

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
''',
}


def main():
    for filepath, content in files.items():
        folder = os.path.dirname(filepath)
        if folder:
            os.makedirs(folder, exist_ok=True)
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"Created file: {filepath}")

    print("\\nDone! Next steps:")
    print("  1. pip install build twine")
    print("  2. pip install -e .        (install locally in editable mode to test the CLI)")
    print(f"  3. {COMMAND_NAME} examples/hello.bes     (try the real command!)")


if __name__ == "__main__":
    main()
