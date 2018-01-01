"""Defines a parser for arbitrary expressions.

Unlike simple expressions, they can also contain :
    - Parentheses
    - Functions
"""

from .simple_expression import SimpleExpression

class Expression(SimpleExpression):
    """Defines an expression."""

    def __init__(self, expression):
        super().__init__(self, expression)
    def __str__(self):
        pass
    def __repr__(self):
        pass
    def evaluate(self):
        pass
    def reset(self, expression):
        pass
