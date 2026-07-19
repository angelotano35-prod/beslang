from .ast_nodes import (
    Num, Str, Bool, Null, Var, BinOp, Assign, Print, Flex,
    ErrorStmt, If, While, For
)


class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.pos = 0

    def peek(self):
        return self.tokens[self.pos]

    def advance(self):
        tok = self.tokens[self.pos]
        self.pos += 1
        return tok

    def expect(self, kind, value=None):
        tok = self.advance()
        if tok[0] != kind or (value is not None and tok[1] != value):
            expected = value if value is not None else kind
            raise SyntaxError(
                f"Mali mo boss. Inaasahan ko '{expected}' pero nakuha ko '{tok[1]}'"
            )
        return tok

    def parse_program(self):
        statements = []
        while self.peek()[0] != "EOF":
            statements.append(self.parse_statement())
        return statements

    def parse_block(self):
        self.expect("OP", "{")
        statements = []
        while self.peek() != ("OP", "}"):
            statements.append(self.parse_statement())
        self.expect("OP", "}")
        return statements

    def parse_statement(self):
        tok = self.peek()
        if tok == ("IDENT", "norem"):
            return self.parse_assign()
        elif tok == ("IDENT", "chika"):
            return self.parse_print()
        elif tok == ("IDENT", "flex"):
            return self.parse_flex()
        elif tok == ("IDENT", "shet"):
            return self.parse_shet()
        elif tok == ("IDENT", "kung"):
            return self.parse_if()
        elif tok == ("IDENT", "edi"):
            return self.parse_while()
        elif tok == ("IDENT", "bawat"):
            return self.parse_for()
        else:
            raise SyntaxError(f"Mali mo boss. Hindi ko maintindihan yung '{tok[1]}'")

    def parse_assign(self):
        self.advance()
        name = self.expect("IDENT")[1]
        self.expect("OP", "=")
        expr = self.parse_expr()
        return Assign(name, expr)

    def parse_print(self):
        self.advance()
        self.expect("OP", "(")
        expr = self.parse_expr()
        self.expect("OP", ")")
        return Print(expr)

    def parse_flex(self):
        self.advance()
        self.expect("OP", "(")
        expr = self.parse_expr()
        self.expect("OP", ")")
        return Flex(expr)

    def parse_shet(self):
        self.advance()
        self.expect("OP", "(")
        expr = self.parse_expr()
        self.expect("OP", ")")
        return ErrorStmt(expr)

    def parse_if(self):
        self.advance()  # kung
        self.expect("OP", "(")
        cond = self.parse_expr()
        self.expect("OP", ")")
        then_block = self.parse_block()
        else_block = None
        if self.peek() == ("IDENT", "kundi"):
            self.advance()
            else_block = self.parse_block()
        return If(cond, then_block, else_block)

    def parse_while(self):
        self.advance()  # edi (this is the WHILE keyword now)
        self.expect("OP", "(")
        cond = self.parse_expr()
        self.expect("OP", ")")
        body = self.parse_block()
        return While(cond, body)

    def parse_for(self):
        self.advance()
        var = self.expect("IDENT")[1]
        self.expect("IDENT", "sa")
        start = self.parse_expr()
        self.expect("OP", "..")
        end = self.parse_expr()
        body = self.parse_block()
        return For(var, start, end, body)

    def parse_expr(self):
        return self.parse_comparison()

    def parse_comparison(self):
        left = self.parse_addsub()
        while self.peek()[1] in ("==", "!=", "<", ">", "<=", ">="):
            op = self.advance()[1]
            right = self.parse_addsub()
            left = BinOp(left, op, right)
        return left

    def parse_addsub(self):
        left = self.parse_muldiv()
        while self.peek()[1] in ("+", "-", "at"):
            op = self.advance()[1]
            if op == "at":
                op = "+"
            right = self.parse_muldiv()
            left = BinOp(left, op, right)
        return left

    def parse_muldiv(self):
        left = self.parse_atom()
        while self.peek()[1] in ("*", "/", "%"):
            op = self.advance()[1]
            right = self.parse_atom()
            left = BinOp(left, op, right)
        return left

    def parse_atom(self):
        kind, value = self.advance()
        if kind == "NUMBER":
            return Num(float(value) if "." in value else int(value))
        if kind == "STRING":
            return Str(value[1:-1])
        if kind == "IDENT":
            if value == "omsm":
                return Bool(True)
            if value == "aray mo":
                return Bool(False)
            if value == "alaws":
                return Null()
            return Var(value)
        if (kind, value) == ("OP", "("):
            expr = self.parse_expr()
            self.expect("OP", ")")
            return expr
        raise SyntaxError(f"Mali mo boss. Hindi ko alam 'to: {value}")
