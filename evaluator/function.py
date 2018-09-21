'''Defines a parser for arbitrary functions with one variable.'''

# TODO : Generalise for multi-variable functions

from .expression import Expression

class Function:
    '''Defines a function.'''

    def __init__(self, expression):
        self.expression = expression

    def eval(self, val):
        '''Evaluate the function.'''

        expression = self.expression.replace('x', str(val))
        return Expression(expression).eval()

    def __call__(self, val):
        return self.eval(val)
