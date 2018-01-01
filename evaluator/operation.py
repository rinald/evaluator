"""Defines a class for mathematical operations."""

from .helpers import OPERATORS

class Operation:
    """Mathematical operation."""

    def __init__(self, left, operator, right):
        self.left = left
        self.operator = operator
        self.right = right
    def __str__(self):
        return "({}{}{})".format(self.left, self.operator, self.right)
    def __repr__(self):
        return self.__str__()
    def evaluate(self):
        """Evaluate operation."""

        function = OPERATORS[self.operator]["function"]
        return function(self.left, self.right)
