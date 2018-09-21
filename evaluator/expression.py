'''Defines a parser for arbitrary expressions.'''

# from .errors import ParsingError, EvaluationError
# from .operation import Operation
# from .util import OPERATORS, CONSTANTS

class Expression:
    '''Defines an expression.'''

    def __init__(self, expression):
        self.expression = expression

    def _build(self):
        '''Build the AST (Operation Tree).'''

        pass

    def eval(self):
        '''Evaluate the expression.'''

        pass
