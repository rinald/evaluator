"""Defines evaluator errors."""

class EvaluationError(Exception):
    """Raised when the expression can't be evaluated."""

    pass

class ParsingError(Exception):
    """Raised when a token can't be parsed."""

    pass

class ReadingError(Exception):
    """Raised when the lexer doesn't know how to interpret a character."""

    pass
