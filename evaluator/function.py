'''Defines the Function object.'''

from .parser import Parser
from .operation import Operation

class Function:
    '''Defines a function.'''

    def __init__(self, expression):
        self.expression = expression

    def eval(self, **kwargs):
        '''Evaluate the function.'''

        self.ast = Parser(self.expression, vars_=kwargs).parse()

        if isinstance(self.ast, Operation):
            return self.ast.eval()
        else:
            return self.ast

    def __call__(self, **kwargs):
        return self.eval(**kwargs)
