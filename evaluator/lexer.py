'''Defines a lexer for mathematical expressions.'''

from .token import Token
from .errors import ReadError
from .util import is_digit, is_operator, is_whitespace, is_letter, is_bracket
from .util import CONSTANTS, OPERATORS

class Lexer:
    '''Lexer for mathematical expressions.'''

    EOI = '' # end of input

    def __init__(self, expression):
        self.expression = expression
        self.cursor_at = 0
        self.read_from = 0
        self.current = expression[0] # character under cursor

    def ignore_whitespace(self):
        '''Ignore whitespace characters.'''

        while is_whitespace(self.current):
            self.move()
        
        self.read_from = self.cursor_at

    def move(self):
        '''Move cursor forward.'''

        self.cursor_at += 1

        if self.cursor_at <= len(self.expression) - 1:
            self.current = self.expression[self.cursor_at]
        else:
            self.current = Lexer.EOI
    
    def peek(self):
        '''Peek next token.'''

        self.ignore_whitespace()

        token = self.read()
        self.cursor_at = self.read_from
        if self.current != Lexer.EOI:
            self.current = self.expression[self.cursor_at] # reset cursor after read()
        return token

    def next(self):
        '''Return next token.'''

        self.ignore_whitespace()
        
        token = self.read()
        self.read_from = self.cursor_at
        return token
        
    def read(self):
        '''Read next token.'''

        if self.current == Lexer.EOI: # reached end of input
            return None

        # First we get generic types
        if is_digit(self.current):
            while is_digit(self.current):
                self.move()
            generic_type = 'number'
        elif is_letter(self.current):
            while is_letter(self.current):
                self.move()
            generic_type = 'identifier'
        elif is_operator(self.current):
            self.move()
            generic_type = 'operator'
        elif is_bracket(self.current):
            self.move()
            generic_type = 'bracket'
        else:
            raise ReadError('Invalid character \'{}\''.format(self.current))

        value = self.expression[self.read_from:self.cursor_at]

        # Then we return specific types based on the value
        if generic_type == 'number':
            if '.' in value:
                type_ = 'decimal'
            else:
                type_ = 'integer'
        elif generic_type == 'identifier':
            if value in OPERATORS['prefix']: # functions are just prefix operators
                type_ = 'function'
            elif value in CONSTANTS:
                type_ = 'constant'
            else:
                type_ = 'variable' # all that's left is considered a variable
        elif generic_type == 'bracket':
            if value == '(':
                type_ = 'left_round'
            elif value == ')':
                type_ = 'right_round'
            elif value == '[':
                type_ = 'left_square'
            elif value == ']':
                type_ = 'right_square'
            elif value == '{':
                type_ = 'left_curly'
            elif value == '}':
                type_ = 'right_curly'
            elif value == '<':
                type_ = 'left_angular'
            elif value == '>':
                type_ = 'right_angular'
        else:
            type_ = 'operator' # operators are just operators

        return Token(type_, value)
