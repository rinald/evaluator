"""Defines a class for mathematical operations."""

from .helpers import OPERATORS

class Operation:
    """Defines a mathematical operation."""

    def __init__(self, left, operator, right, type_="infix"):
        self.type = type_
        self.left = left
        self.operator = operator
        self.right = right
        
    def __str__(self):
        return "({}{}{})".format(self.left, self.operator, self.right)
    def __repr__(self):
        return self.__str__()
