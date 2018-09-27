'''Defines tokens for mathematical expressions.'''

class Token:
    '''Token for mathematical expressions.

    Provides type and value to the lexer.
    '''

    def __init__(self, type_, value):
        self.type = type_
        self.value = value
    
    def __str__(self):
        return '<token {} \'{}\'>'.format(self.type, self.value)
    
    def __repr__(self):
        return self.__str__()
    
