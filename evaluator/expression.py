"""Defines a parser for arbitrary expressions.

Unlike simple expressions, they can also contain :
    - Parentheses
    - Functions
"""

from .lexer import Lexer
from .operation import Operation
from .helpers import OPERATORS

class Expression:
    """Defines an expression."""

    def __init__(self, expression):
        self.expression = expression
        self._init()
    def __str__(self):
        pass
    def __repr__(self):
        pass
    def _init(self):
        """Do the actual initialisation."""

        pass
    def _evaluate(self, node):
        """Do the actual evaluation."""

        pass
    def evaluate(self):
        """Evaluate expression."""

        pass
    def reset(self, expression):
        """Reset expression."""
        
        pass
