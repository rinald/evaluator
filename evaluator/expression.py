"""Defines a parser for arbitrary expressions."""

from .simple_expression import SimpleExpression
from .errors import ParsingError, EvaluationError
from .operation import Operation
from .helpers import OPERATORS

class Expression(SimpleExpression):
    """Defines an expression."""

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
                    operands.append(Expression(token.value[1:-1]))
                elif isinstance(operands[-1], Operation):
                    if operands[-1].type == "prefix":
                        operands[-1].right = Expression(token.value[1:-1])
                    else:
                        raise ParsingError
                else:
                    operands.append(Expression(token.value[1:-1]))
            else:
                raise error
    def _eval(self, node):
        try:
            return super()._eval(node)
        except EvaluationError as error:
            if isinstance(node, Expression):
                return self._eval(node.root)
            else:
                raise error
