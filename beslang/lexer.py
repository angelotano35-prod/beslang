import re

TOKEN_SPEC = [
    ("NUMBER",  r"\d+(\.\d+)?"),
    ("STRING",  r'"[^"]*"'),
    ("OP",      r"==|!=|<=|>=|\.\.|[+\-*/%=<>(),{}]"),
    ("COMMENT", r"skl[^\n]*"),
    ("IDENT",   r"[A-Za-z_][A-Za-z0-9_]*"),
    ("SKIP",    r"[ \t]+"),
    ("NEWLINE", r"\n"),
    ("MISMATCH", r"."),
]

MASTER_PATTERN = "|".join(f"(?P<{name}>{pattern})" for name, pattern in TOKEN_SPEC)

MULTIWORD_KEYWORDS = [
    (["aray", "mo"], "aray mo"),
]


def tokenize(source):
    tokens = []
    for match in re.finditer(MASTER_PATTERN, source):
        kind = match.lastgroup
        value = match.group()
        if kind in ("SKIP", "COMMENT", "NEWLINE"):
            continue
        if kind == "MISMATCH":
            raise SyntaxError(f"Mali mo boss. Ano itong character na 'to: {value!r}")
        tokens.append((kind, value))
    tokens.append(("EOF", None))
    return _merge_multiword_keywords(tokens)


def _merge_multiword_keywords(tokens):
    merged = []
    i = 0
    while i < len(tokens):
        matched = False
        for words, combined in MULTIWORD_KEYWORDS:
            n = len(words)
            if all(
                i + j < len(tokens)
                and tokens[i + j][0] == "IDENT"
                and tokens[i + j][1] == words[j]
                for j in range(n)
            ):
                merged.append(("IDENT", combined))
                i += n
                matched = True
                break
        if not matched:
            merged.append(tokens[i])
            i += 1
    return merged
