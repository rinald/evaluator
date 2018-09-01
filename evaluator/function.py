'''Defines a parser for arbitrary functions with one variable.'''

from .errors import ParsingError, EvaluationError
from .operation import Operation
from .util import OPERATORS, CONSTANTS

class Function:
    '''Defines a function.'''

    def __init__(self, expression):
        pass

    def _parse(self, token):
        '''Parse a token.'''
        
        pass

    def _init(self):
        '''Initialise Function AST (Operation Tree).'''
        
        pass

    def eval(self, val):
        '''Evaluate the function.'''
        
        pass

    def __call__(self, val):
        return self.eval(val)
