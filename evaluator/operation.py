'''Defines a class for mathematical operations.'''

from .token import Token
from .errors import EvaluateError
from .util import OPERATORS, CONSTANTS

def simplify(node, vars_):
    if isinstance(node, Operation):
        value = node.eval(vars_)
    elif isinstance(node, str):
        variable = node
        
        if vars_ == None:
            raise EvaluateError('Expressions can\'t have variables.')
        elif variable not in vars_:
            raise EvaluateError('Variable {} not initialised.'.format(variable))
        else:
            value = vars_[variable]
    else:
        value = node
        
    return value

class Operation:
    '''Defines a mathematical operation.'''

    def __init__(self, operator, left=None, right=None):  
        self.operator = operator
        self.left = left
        self.right = right

        if left != None and right != None:
            self.type = 'infix'
        elif left == None and right != None:
            self.type = 'prefix'
        elif left != None and right == None:
            self.type = 'postfix'
        else:
            self.type = 'undefined'

    def __str__(self):
        return '({}{}{})'.format(
            self.left if self.left is not None else '',
            self.operator,
            self.right if self.right is not None else ''
        )

    def __repr__(self):
        return self.__str__()

    def eval(self, vars_=None):
        '''Evaluate the operation.'''

        function = OPERATORS[self.type][self.operator]['function']

        if self.type == 'infix':
            left = simplify(self.left, vars_)
            right = simplify(self.right, vars_)

            return function(left, right)

        elif self.type == 'prefix':
            right = simplify(self.right, vars_)

            return function(right)

        elif self.type == 'postfix':
            left = simplify(self.left, vars_)

            return function(left)

        else:
            raise EvaluateError('Cannot evaluate operation of type \'undefined\'.')
