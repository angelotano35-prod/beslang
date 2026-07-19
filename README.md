# BesLang

A real, from-scratch programming language interpreter (not a Python transpiler)
using custom Filipino/Taglish words for its keywords, with a lexer, parser, and
tree-walking evaluator all written in Python.

## Keywords

| BesLang               | Meaning |
|--------------------------|---------|
| `norem x = 5`             | Declare/assign a variable |
| `chika(...)`              | Print |
| `flex(...)`               | Print with decorative border |
| `shet(...)`               | Raise a runtime error with a custom message |
| `kung (cond) { }`         | If |
| `kundi { }`               | Else |
| `edi (cond) { }`          | While loop |
| `bawat i sa a..b { }`     | For loop, i goes from a to b inclusive |
| `omsm` / `aray mo`        | True / False |
| `alaws`                   | Null |
| `at`                      | Concatenation / addition |
| `skl ...`                 | Comment |

## Custom error messages

| Situation | Message |
|-----------|---------|
| Undefined variable | `Kelan ba naging 'x' ang 'x'?` |
| Division by zero | `Zero yan eh oh zero, wag kana mag code yoko na` |
| Type mismatch (e.g. number + wrong type) | `MISMATCH NGANIIIII` |
| General syntax error | `Mali mo boss. ...` |

## Running a program

```bash
python run.py examples/hello.bes
python run.py examples/fizzbuzz.bes
python run.py examples/error_handling.bes
python run.py examples/null_demo.bes
python run.py examples/undefined_var_demo.bes
python run.py examples/divide_by_zero_demo.bes
```

## Architecture

- **`lexer.py`** - tokenizes raw `.bes` source text into a stream of tokens
- **`parser.py`** - recursive descent parser, builds an Abstract Syntax Tree (AST) from tokens
- **`interpreter.py`** - tree-walking evaluator, walks the AST and executes it directly

No `exec()`, no Python syntax reuse under the hood - this is a genuine, if small,
programming language implementation.

## Current limitations (intentionally kept simple for now)

- No functions/return yet
- No break/continue yet
- No lists/arrays yet
