"""Defines a parser for functions with one variable (x)."""

from .simple_function import SimpleFunction
from .errors import ParsingError, EvaluationError

class Function(SimpleFunction):
    """Defines a function."""

    def __init__(self, expression):
        super().__init__(expression)
    def _append_token(self, token, operands, operations):
        try:
            super()._append_token(token, operands, operations)
        except ParsingError as error:
            token = error.args[0]
            if token.type == "expression":
                operands.append(Function(token.value[1:-1]))
            else:
                raise error
    def _evaluate(self, node, x):
        try:
            return super()._evaluate(node, x)
        except EvaluationError as error:
            node = error.args[0]
            if isinstance(node, Function):
                return self._evaluate(node.root, x)
            else:
                raise error
