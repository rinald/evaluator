'''Defines a class for mathematical operations.'''

from .util import OPERATORS
from .errors import EvaluateError

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

    def eval(self):
        '''Evaluate the operation.'''

        function = OPERATORS[self.type][self.operator]['function']

        if self.type == 'infix':
            if isinstance(self.left, Operation):
                left = self.left.eval()
            else:
                left = self.left

            if isinstance(self.right, Operation):
                right = self.right.eval()
            else:
                right = self.right

            return function(left, right)

        elif self.type == 'prefix':
            if isinstance(self.right, Operation):
                right = self.right.eval()
            else:
                right = self.right

            return function(right)

        elif self.type == 'postfix':
            if isinstance(self.left, Operation):
                left = self.left.eval()
            else:
                left = self.left

            return function(left)

        else:
            raise EvaluateError('Cannot evaluate operation of type \'undefined\'.')
