"""Defines a parser for functions with one variable (x)."""

from .expression import Expression

class Function(Expression):
    """Defines a function."""

    def __init__(self, functional_expression):
        super().__init__(self, functional_expression)
    def __str__(self):
        pass
    def __repr__(self):
        pass
    def __call__(self, x):
        pass
    def evaluate(self, x):
        pass
    def reset(self, functional_expression):
        pass
    