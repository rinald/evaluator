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

<<<<<<< HEAD
    def __next__(self):
        # Ignore whitespace
        if is_whitespace(self.current_character):
            while is_whitespace(self.current_character):
                self.read_character()
            self.reading_position = self.cursor_position
        
        if self.current_character == Lexer.EOI:
            raise StopIteration
        
        return self.get_token()
=======
        token = self.read()
        self.cursor_at = self.read_from
        if self.current != Lexer.EOI:
            self.current = self.expression[self.cursor_at]
        return token

    def next(self):
        '''Return next token.'''

        self.ignore_whitespace()
        
        token = self.read()
        self.read_from = self.cursor_at
        return token
        
    def read(self):
        '''Read next token.'''
>>>>>>> rewrite

        if self.current == Lexer.EOI:
            return None

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

        # Return specific types
        if generic_type == 'number':
            if '.' in value:
                type_ = 'decimal'
            else:
                type_ = 'integer'
        elif generic_type == 'identifier':
            if value in OPERATORS['prefix']:
                type_ = 'function'
            elif value in CONSTANTS:
                type_ = 'constant'
            else:
                type_ = 'variable'
        elif generic_type == 'bracket':
            if value == '(':
                type_ = 'left_parenthesis'
            elif value == ')':
                type_ = 'right_parenthesis'
            elif value == '[':
                type_ = 'left_bracket'
            elif value == ']':
                type_ = 'right_bracket'
            elif value == '{':
                type_ = 'left_brace'
            elif value == '}':
                type_ = 'right_brace'
            elif value == '<':
                type_ = 'left_angular'
            elif value == '>':
                type_ = 'right_angular'
        else:
            type_ = 'operator'

        return Token(type_, value)
