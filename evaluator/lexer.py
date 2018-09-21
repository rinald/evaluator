'''Defines a lexer for mathematical expressions.'''

from .token import Token
from .errors import ReadError
from .util import is_digit, is_operator, is_whitespace, is_letter

class Lexer:
    '''Lexer for mathematical expressions.

    Iterable that iterates through tokens.
    '''

    EOI = '' # End Of Input

    def __init__(self, expression):
        self.expression = expression
        self.cursor_position = 0
        self.reading_position = 0 # Position to start reading from
        self.current_character = expression[0]

    def __iter__(self):
        return self

    def __next__(self):
        # Ignore whitespace
        if is_whitespace(self.current_character):
            while is_whitespace(self.current_character):
                self.read_character()
            self.reading_position = self.cursor_position

        if self.current_character == Lexer.EOI:
            raise StopIteration

        return self.get_token()

    def read_character(self):
        '''Reads next character.'''

        self.cursor_position += 1

        if self.cursor_position <= len(self.expression) - 1:
            self.current_character = self.expression[self.cursor_position]
        else:
            self.current_character = Lexer.EOI

    def get_token(self):
        '''Return next token.'''

        if is_digit(self.current_character):
            while is_digit(self.current_character):
                self.read_character()
            token_type = 'number'
        elif is_letter(self.current_character):
            while is_letter(self.current_character):
                self.read_character()
            token_type = 'identifier'
        elif is_operator(self.current_character):
            self.read_character()
            token_type = 'operator'
        elif self.current_character == '(': ### Special case
            depth = 0
            self.read_character() # Move cursor inside expression
            while not (self.current_character == ')' and depth == 0):
                if self.current_character == '(':
                    depth += 1
                if self.current_character == ')':
                    depth -= 1
                self.read_character()
            self.read_character() # Move cursor outside expression
            token_type = 'expression'
        else:
            raise ReadError('Invalid character "{}"'.format(self.current_character))

        value = self.expression[self.reading_position:self.cursor_position]
        self.reading_position = self.cursor_position

        return Token(token_type, value)
