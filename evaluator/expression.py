"""Defines a parser for arbitrary expressions.

Currently only operators, integers and parentheses are allowed.
For negative integers you have to write (0-i), where i is a positive integer.
"""

from .simple_expression import SimpleExpression
from .errors import ParsingError, EvaluationError

class Expression(SimpleExpression):
    """Defines an expression."""

    def __init__(self, expression):
        super().__init__(expression)
    def _append_token(self, token, operands, operations):
        try:
            super()._append_token(token, operands, operations)
        except ParsingError as error:
            token = error.args[0]
            if token.type == "expression":
                operands.append(Expression(token.value[1:-1]))
            else:
                raise error
    def _evaluate(self, node):
        try:
            return super()._evaluate(node)
        except EvaluationError as error:
            node = error.args[0]
            if isinstance(node, Expression):
                return self._evaluate(node.root)
            else:
                raise error
