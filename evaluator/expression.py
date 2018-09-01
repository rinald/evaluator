'''Defines a parser for arbitrary expressions.'''

from .errors import ParsingError, EvaluationError
from .operation import Operation
from .util import OPERATORS, CONSTANTS

class Expression:
    '''Defines an expression.'''
    
    def __init__(self, expression):
        pass

    def _parse(self, token):
        '''Parse a token.'''
        
        pass

    def _init(self):
        '''Initialise Expression AST (Operation Tree).'''
        
        pass

    def eval(self):
        '''Evaluate the expression.'''
        
        pass
