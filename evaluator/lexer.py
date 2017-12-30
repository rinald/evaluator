"""Defines a lexer for mathematical expressions."""

def is_digit(character):
    """Checks if character is a digit."""

    return character != "" and character in "0123456789"

def is_operator(character):
    """Checks if character is an operator."""

    return character != "" and character in "+-*/%^"

def is_parenthese(character):
    """Checks if character is a parenthese."""

    return character != "" and character in "()"

def is_whitespace(character):
    """Checks if character is a whitespace."""

    return character != "" and character in " \n\t"

class Token:
    """Token for mathematical expressions.

    Provides type and value to the lexer.
    """

    def __init__(self, type_, value):
        self.type = type_
        self.value = value

    def __str__(self):
        return "{} : {}".format(self.type, self.value)

class TokenError(Exception):
    """Raised when reading an invalid value."""

    pass

class Lexer:
    """Lexer for mathematical expressions.

    Iterable that iterates through tokens.
    """

    EOI = "" # End Of Input

    def __init__(self, expression):
        self.expression = expression
        self.cursor_position = 0
        self.reading_position = 0 # Position to start reading from
        self.current_character = expression[0]

    def __iter__(self):
        return self

    def __next__(self):
        if self.current_character == Lexer.EOI:
            raise StopIteration

        if is_digit(self.current_character):
            while is_digit(self.current_character):
                self.read_character()
            type_ = "integer"
            value = self.expression[self.reading_position : self.cursor_position]
            self.reading_position = self.cursor_position
            return Token(type_, value)
        elif is_operator(self.current_character):
            self.read_character()
            type_ = "operator"
            value = self.expression[self.reading_position : self.cursor_position]
            self.reading_position = self.cursor_position
            return Token(type_, value)
        elif is_parenthese(self.current_character):
            self.read_character()
            type_ = "parenthese"
            value = self.expression[self.reading_position : self.cursor_position]
            self.reading_position = self.cursor_position
            token = Token(type_, value)
            return token
        elif is_whitespace(self.current_character):
            self.read_character()
        else:
            raise TokenError("Invalid value.")

    def read_character(self):
        """Reads next character."""

        self.cursor_position += 1
        if self.cursor_position <= len(self.expression) - 1:
            self.current_character = self.expression[self.cursor_position]
        else:
            self.current_character = Lexer.EOI

    def read_token(self):
        """Reads next token."""

        pass
