'''Defines the Expression object.'''

from .parser import Parser
from .operation import Operation

class Expression:
    '''Defines an expression.'''

    def __init__(self, expression):
        self.expression = expression
    
    def eval(self):
        '''Evaluate the expression.'''
        
        self.ast = Parser(self.expression).parse()

        if isinstance(self.ast, Operation):
            return self.ast.eval()
        else:
            return self.ast