'''Defines the Function object.'''

from .parser import Parser
from .operation import simplify

class Function:
    '''Defines a function.'''

    def __init__(self, expression):
        self.expression = expression
        self.ast = Parser(expression).parse()

    def __str__(self):
        return '<function \'{}\'>'.format(self.expression)

    def __repr__(self):
        return self.__str__()

    def eval(self, **kwargs):
        '''Evaluate the function.'''

        return simplify(self.ast, vars_=kwargs)

    def __call__(self, **kwargs):
        return self.eval(**kwargs)
