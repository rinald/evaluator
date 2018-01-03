"""Defines a parser for simple functions with one variable.

A simple function has no parentheses.
"""

from .helpers import OPERATORS
from .operation import Operation
from .simple_expression import SimpleExpression
from .errors import ParsingError, EvaluationError

class SimpleFunction(SimpleExpression):
    """Defines a simple function."""

    def __init__(self, expression):
        super().__init__(expression)
    def __str__(self):
        return "<function : {}>".format(self.expression)
    def __call__(self, x):
        return self.evaluate(x)
    def _append_token(self, token, operands, operations):
        try:
            super()._append_token(token, operands, operations)
        except ParsingError as error:
            token = error.args[0]
            if token.type == "variable":
                operands.append(token.value)
            else:
                raise error
    def _evaluate(self, node, x):
        if isinstance(node, int):
            return node
        elif node == "x":
            return x
        elif isinstance(node, Operation):
            function = OPERATORS[node.operator]["function"]
            left = self._evaluate(node.left, x)
            right = self._evaluate(node.right, x)
            return function(left, right)
        else:
            raise EvaluationError(node)
    def evaluate(self, x):
        return self._evaluate(self.root, x)
