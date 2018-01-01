"""Defines a parser for simple expressions.

A simple expression has no parentheses.
"""

from .lexer import Lexer
from .operation import Operation
from .helpers import OPERATORS

class SimpleExpression:
    """Defines a simple expression."""

    def __init__(self, simple_expression):
        self.expression = simple_expression
        self.init_tree(simple_expression)
        print(self.root)
    def __str__(self):
        return "Expression : ({})".format(self.expression)
    def __repr__(self):
        pass

    def init_tree(self, simple_expression):
        """Do the actual initialisation."""

        operands = [] # Will contain operands as integers
        operations = [] # Will contain operations

        lexer_ = Lexer(simple_expression)

        for token in lexer_:
            if token.type == "integer":
                operands.append(int(token.value))
            elif token.type == "operator":
                operations.append(Operation(None, token.value, None))
            else:
                pass

        while operations != []:
            # Associate operands with operations
            # Always associate the firsts with the lasts
            operations[0].left = operands[0]
            operations[-1].right = operands[-1]
            # Associate the middle operands
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

        # Assign the root operation
        self.root = operands[0]

    def evaluate(self):
        """Evaluate expression."""

        pass
    def reset(self, simple_expression):
        """Reset expression."""

        pass
  