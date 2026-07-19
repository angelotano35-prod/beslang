import sys
from beslang.lexer import tokenize
from beslang.parser import Parser
from beslang.interpreter import Interpreter, BesLangError


def run_file(filepath):
    with open(filepath, "r", encoding="utf-8") as f:
        source = f.read()

    try:
        tokens = tokenize(source)
        parser = Parser(tokens)
        statements = parser.parse_program()
        interpreter = Interpreter()
        interpreter.run(statements)
    except BesLangError as e:
        print(f"\nOops! {e}")
    except SyntaxError as e:
        print(f"\nOops! {e}")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python run.py <file.bes>")
        sys.exit(1)
    run_file(sys.argv[1])
