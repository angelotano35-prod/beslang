from .ast_nodes import Num, Str, Bool, Null, Var, BinOp, Assign, Print, Flex, ErrorStmt, If, While, For


class BesLangError(Exception):
    pass


class Interpreter:
    def __init__(self):
        self.vars = {}

    def run(self, statements):
        for stmt in statements:
            self.execute(stmt)

    def execute(self, stmt):
        if isinstance(stmt, Assign):
            self.vars[stmt.name] = self.evaluate(stmt.expr)
        elif isinstance(stmt, Print):
            print(self.evaluate(stmt.expr))
        elif isinstance(stmt, Flex):
            val = self.evaluate(stmt.expr)
            print("=" * 24)
            print(val)
            print("=" * 24)
        elif isinstance(stmt, ErrorStmt):
            msg = self.evaluate(stmt.message_expr)
            raise BesLangError(msg)
        elif isinstance(stmt, If):
            if self.evaluate(stmt.cond):
                self.run(stmt.then_block)
            elif stmt.else_block is not None:
                self.run(stmt.else_block)
        elif isinstance(stmt, While):
            while self.evaluate(stmt.cond):
                self.run(stmt.body)
        elif isinstance(stmt, For):
            start = self.evaluate(stmt.start)
            end = self.evaluate(stmt.end)
            for i in range(int(start), int(end) + 1):
                self.vars[stmt.var] = i
                self.run(stmt.body)
        else:
            raise BesLangError(f"Mali mo boss. Hindi ko alam paano i-execute 'to: {stmt}")

    def evaluate(self, expr):
        if isinstance(expr, Num):
            return expr.value
        if isinstance(expr, Str):
            return expr.value
        if isinstance(expr, Bool):
            return expr.value
        if isinstance(expr, Null):
            return None
        if isinstance(expr, Var):
            if expr.name not in self.vars:
                raise BesLangError(f"Kelan ba naging '{expr.name}' ang '{expr.name}'?")
            return self.vars[expr.name]
        if isinstance(expr, BinOp):
            left = self.evaluate(expr.left)
            right = self.evaluate(expr.right)
            op = expr.op
            try:
                if op == "+":
                    return left + right
                if op == "-":
                    return left - right
                if op == "*":
                    return left * right
                if op == "/":
                    if right == 0:
                        raise BesLangError("Zero yan eh oh zero, wag kana mag code yoko na")
                    return left / right
                if op == "%":
                    return left % right
                if op == "==":
                    return left == right
                if op == "!=":
                    return left != right
                if op == "<":
                    return left < right
                if op == ">":
                    return left > right
                if op == "<=":
                    return left <= right
                if op == ">=":
                    return left >= right
            except TypeError:
                raise BesLangError("MISMATCH NGANIIIII")
        raise BesLangError(f"Mali mo boss. Hindi ko alam i-evaluate 'to: {expr}")
