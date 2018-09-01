'''Defines a class for mathematical operations.'''

from .util import OPERATORS

class Operation:
    '''Defines a mathematical operation.'''

    def __init__(self, left, operator, right):
        self.left = left
        self.operator = operator
        self.right = right

        if self.left is not None and self.right is not None:
            self.type = 'infix'
        elif self.left is None and self.right is not None:
            self.type = 'prefix'
        elif self.left is not None and self.right is None:
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
