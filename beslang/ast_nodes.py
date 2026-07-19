class Num:
    def __init__(self, value):
        self.value = value


class Str:
    def __init__(self, value):
        self.value = value


class Bool:
    def __init__(self, value):
        self.value = value


class Null:
    pass


class Var:
    def __init__(self, name):
        self.name = name


class BinOp:
    def __init__(self, left, op, right):
        self.left = left
        self.op = op
        self.right = right


class Assign:
    def __init__(self, name, expr):
        self.name = name
        self.expr = expr


class Print:
    def __init__(self, expr):
        self.expr = expr


class Flex:
    def __init__(self, expr):
        self.expr = expr


class ErrorStmt:
    def __init__(self, message_expr):
        self.message_expr = message_expr


class If:
    def __init__(self, cond, then_block, else_block):
        self.cond = cond
        self.then_block = then_block
        self.else_block = else_block


class While:
    def __init__(self, cond, body):
        self.cond = cond
        self.body = body


class For:
    def __init__(self, var, start, end, body):
        self.var = var
        self.start = start
        self.end = end
        self.body = body
