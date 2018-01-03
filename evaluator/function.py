"""Defines a parser for arbitrary functions with one variable.

Currently only operators, integers, parentheses and 'x' are allowed.
For negative integers you have to write (0-i), where i is a positive integer.
"""

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
