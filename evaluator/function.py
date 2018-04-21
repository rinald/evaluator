"""Defines a parser for arbitrary functions with one variable.

Currently only operators, integers, parentheses and 'x' are allowed.
For negative integers you have to write (0-i), where i is a positive integer.
"""

from .simple_function import SimpleFunction
from .errors import ParsingError, EvaluationError
from .operation import Operation
from .helpers import OPERATORS

class Function(SimpleFunction):
    """Defines a function."""

    def __init__(self, expression):
        super().__init__(expression)
    def _append_token(self, token, operands, operations):
        try:
            super()._append_token(token, operands, operations)
        except ParsingError as error:
            if token.type == "identifier":
                if token.value in OPERATORS:
                    operands.append(Operation(None, token.value, None, type_="prefix"))
                else:
                    raise ParsingError("Invalid identifier.")
            elif token.type == "expression":
                if len(operands) == 0:
                    operands.append(Function(token.value[1:-1]))
                elif isinstance(operands[-1], Operation):
                    if operands[-1].type == "prefix":
                        operands[-1].right = Function(token.value[1:-1])
                    else:
                        raise ParsingError
                else:
                    operands.append(Function(token.value[1:-1]))
            else:
                raise error
    def _eval(self, node, x):
        try:
            return super()._eval(node, x)
        except EvaluationError as error:
            if isinstance(node, Function):
                return self._eval(node.root, x)
            else:
                raise error
