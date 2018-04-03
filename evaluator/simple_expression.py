"""Defines a parser for simple expressions.

A simple expression has no parentheses.
"""

from .lexer import Lexer
from .helpers import OPERATORS
from .operation import Operation
from .errors import ParsingError, EvaluationError

class SimpleExpression:
    """Defines a simple expression."""

    def __init__(self, expression):
        self.expression = expression
        self._init(expression)
    def __str__(self):
        return "<expression '{}'>".format(self.expression)
    def __repr__(self):
        return self.__str__()
    def _append_token(self, token, operands, operations):
        if token.type == "integer":
            operands.append(int(token.value))
        elif token.type == "operator":
            operations.append(Operation(None, token.value, None))                     
        else:
            raise ParsingError(token)
    def _init(self, expression):
        """Do the actual initialisation."""

        operands = [] # Will contain operands as integers
        operations = [] # Will contain operations

        lexer = Lexer(expression)

        for token in lexer:
            self._append_token(token, operands, operations)

        while operations != []:
            operations[0].left = operands[0]
            operations[-1].right = operands[-1]

            for i in range(1, len(operands) - 1):
                left_priority = OPERATORS[operations[i-1].operator]["priority"]
                right_priority = OPERATORS[operations[i].operator]["priority"]

                if left_priority >= right_priority:
                    operations[i-1].right = operands[i]
                else:
                    operations[i].left = operands[i]

            operands_ = []
            operations_ = []
            
            for operation in operations:
                if (operation.left is not None) and (operation.right is None):
                    operands_.append(operation.left)
                    operations_.append(operation)
                elif (operation.left is None) and (operation.right is not None):
                    operands_.append(operation.right)
                    operations_.append(operation)
                elif (operation.left is not None) and (operation.right is not None):
                    operands_.append(operation)
                else:
                    operations_.append(operation)

            operands = operands_
            operations = operations_

        self.root = operands[0]
    def _evaluate(self, node):
        """Do the actual initialisation."""

        if isinstance(node, int):
            return node
        elif isinstance(node, Operation):
            function = OPERATORS[node.operator]["function"]
            
            if node.type == "infix":
                left = self._evaluate(node.left)
                right = self._evaluate(node.right)
                return function(left, right)
            elif node.type == "prefix":
                right = self._evaluate(node.right)
                return function(right)
            else: # node.type == "postfix"
                left = self._evaluate(node.left)
                return function(left)
        else:
            raise EvaluationError(node)

    def evaluate(self):
        """Evaluate expression."""

        return self._evaluate(self.root)
    def reset(self, expression):
        """Reset expression."""

        self.__init__(expression)
