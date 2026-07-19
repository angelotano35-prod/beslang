import sys
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
        print(f"\nOops! {e}")
        sys.exit(1)
    except SyntaxError as e:
        print(f"\nOops! {e}")
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
