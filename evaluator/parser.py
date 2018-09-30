'''Defines the parser to be used by Expression and Function.'''

from .lexer import Lexer
from .errors import ParseError
from .operation import Operation
from .util import OPERATORS, CONSTANTS, MAX_BP

# TODO - Check for mismatched brackets

class Parser:
    def __init__(self, expression):
        self.expression = expression
        self.lexer = Lexer(expression)
        self.depth = 0

    def bp(self, token):
        '''Return binding power of token.'''

        if token == None:
            return -1
        if token.type == 'operator':
            operator = token.value
            if operator in OPERATORS['postfix']:
                return self.depth * MAX_BP + OPERATORS['postfix'][operator]['bp']
            else:
                return self.depth * MAX_BP + OPERATORS['infix'][operator]['bp']
        elif token.type == 'function':
            function = token.value
            return self.depth * MAX_BP + OPERATORS['prefix'][function]['bp']
        elif token.value == ')' or token.value == ']' or token.value == '}' or token.value == '>':
            self.lexer.next()
            self.depth -= 1
            return -1
        else:
            return -1

    def nud(self, token):
        '''Parse token with no left context.'''

        parse = self.parse
        bp = self.bp

        if token.type == 'integer':
            integer = token.value
            return int(integer)
        elif token.type == 'decimal':
            decimal = token.value
            return float(decimal)
        elif token.type == 'constant':
            constant = token.value
            return constant
        elif token.type == 'variable':
            variable = token.value
            return variable
        elif token.type == 'operator':
            operator = token.value
            if operator in OPERATORS['prefix']:
                bp_ = self.depth * MAX_BP + OPERATORS['prefix'][operator]['bp']
                return Operation(operator, right=parse(rbp=bp_))
            else:
                raise ParseError('Operator {} is not a prefix operator.'.format(operator))
        elif token.type == 'function':
            function = token.value
            return Operation(function, right=parse(rbp=bp(token)))
        elif token.value == '(':
            self.depth += 1
            return parse(rbp=self.depth*MAX_BP)
        elif token.value == '[':
            self.depth += 1
            return Operation('floor', right=parse(rbp=self.depth*MAX_BP))
        elif token.value == '{':
            self.depth += 1
            return Operation('ceil', right=parse(rbp=self.depth*MAX_BP))
        elif token.value == '<':
            self.depth += 1
            return Operation('abs', right=parse(rbp=self.depth*MAX_BP))
        else:
            return None

    def led(self, left, token):
        '''Parse token with left context.'''

        parse = self.parse
        bp = self.bp

        if token.type == 'operator':
            operator = token.value
            if operator in OPERATORS['postfix']:
                return Operation(operator, left=left)
            else:
                if operator == '^':
                    return Operation(operator, left=left, right=parse(rbp=bp(token)-1))
                else:
                    return Operation(operator, left=left, right=parse(rbp=bp(token)))
        else:
            return None

    def parse(self, rbp=0):
        '''Parse with TDOP algorithm (Pratt Parsing).'''

        lexer = self.lexer
        nud = self.nud
        led = self.led
        bp = self.bp

        left = nud(lexer.next())

        while bp(lexer.peek()) > rbp:
            left = led(left, lexer.next())

        return left
