"""Defines tokens for mathematical expressions."""

# Errors
class TokenError(Exception):
    """Defines a base class for token related errors."""

    pass

class InvalidToken(TokenError):
    """Raised when the lexer reads an invalid token."""

    pass

class UnknownToken(TokenError):
    """Raised when the lexer reads an unknown token.

    For example, since a simple expression can't contain parentheses,
    so we can say that they are unknown tokens in this context.
    """

    pass

class Token:
    """Token for mathematical expressions.

    Provides type and value to the lexer.
    """

    def __init__(self, type_, value):
        self.type = type_
        self.value = value

    def __str__(self):
        return "<token <{}> : '{}'>".format(self.type, self.value)
