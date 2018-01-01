"""Defines a parser for simple functions."""

from .lexer import Lexer
from .operation import Operation
from .helpers import OPERATORS

class SimpleFunction:
    """Defines a simple function."""

    def __init__(self, functional_expression):
        self.expression = functional_expression
        self._init(functional_expression)
    def __str__(self):
        return "<function : {}>".format(self.expression)
    def __repr__(self):
        return self.__str__()
    def __call__(self, x):
        return self.evaluate(x)
    def _init(self, simple_expression):
        """Do the actual initialisation."""

        operands = [] # Will contain operands as integers
        operations = [] # Will contain operations

        lexer = Lexer(simple_expression)

        for token in lexer:
            if token.type == "integer":
                operands.append(int(token.value))
            elif token.type == "variable":
                operands.append(token.value)
            elif token.type == "operator":
                operations.append(Operation(None, token.value, None))
            else:
                pass
        # Build tree
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
    def _evaluate(self, node, x):
        """Do the actual evaluation."""

        if isinstance(node, int):
            return node
        elif node == "x":
            return x
        function = OPERATORS[node.operator]["function"]
        left = self._evaluate(node.left, x)
        right = self._evaluate(node.right, x)
        return function(left, right)
    def evaluate(self, x):
        """Evaluate f(x)."""

        return self._evaluate(self.root, x)

    def reset(self, functional_expression):
        """Reset function."""

        self.__init__(functional_expression)
