"""Defines a parser for arbitrary expressions.

Unlike simple expressions, they can also contain :
    - Parentheses (DONE)
    - Functions (TODO)
"""

from .simple_expression import SimpleExpression, ParsingError, EvaluationError

class Expression(SimpleExpression):
    """Defines an expression."""

    def __init__(self, expression):
        super().__init__(expression)
    def __str__(self):
        return "<expression '{}'>".format(self.expression)
    def _append_token(self, token, operands, operations):
        try:
            super()._append_token(token, operands, operations)
        except ParsingError as error:
            token = error.args[0]
            if token.type == "expression":
                operands.append(Expression(token.value[1:-1]))
            else:
                raise error
    def _evaluate(self, node):
        """Do the actual evaluation."""
        
        try:
            return super()._evaluate(node)
        except EvaluationError as error:
            node = error.args[0]
            if isinstance(node, Expression):
                return self._evaluate(node.root)
            else:
                raise error
