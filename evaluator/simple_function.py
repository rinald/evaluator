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
        return self.eval(x)
    def _append_token(self, token, operands, operations):
        try:
            super()._append_token(token, operands, operations)
        except ParsingError as error:
            if token.type == "identifier":
                if token.value == "x":
                    operands.append(token.value)
                else:
                    raise ParsingError("Invalid identifier.")
            else:
                raise error
    def _eval(self, node, x):
        if isinstance(node, int) or isinstance(node, float):
            return node
        elif node == "x":
            return x
        elif isinstance(node, Operation):
            function = OPERATORS[node.operator]["function"]
            
            if node.type == "infix":
                left = self._eval(node.left, x)
                right = self._eval(node.right, x)
                return function(left, right)
            elif node.type == "prefix":
                right = self._eval(node.right, x)
                return function(right)
            else: # node.type == "postfix"
                left = self._eval(node.left, x)
                return function(left)
        else:
            raise EvaluationError(node)
    def eval(self, x):
        return self._eval(self.root, x)
