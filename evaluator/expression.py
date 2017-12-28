"""Defines a parser for arbitrary expressions. 

Unlike elementary expressions, they can also contain :
    - Parentheses
    - Functions
"""

from .elementary_expression import Elementary_Expression

class Expression(Elementary_Expression):
    def __init__(self, experssion):
        pass
    def __str__(self):
        pass
    def __repr__(self):
        pass
    def evaluate(self):
        pass
    def reset(self, expression):
        pass
