'''Defines utility functions and structures.'''

import math
import operator

def is_digit(character):
    '''Checks if character is a digit.'''

    return character != '' and character in '0123456789.'

def is_letter(character):
    '''Checks if character is a (lowercase) letter.'''

    return character != '' and character in 'abcdefghijklmnopqrstuvwxyz'

def is_operator(character):
    '''Checks if character is an operator.'''

    return character != '' and character in '+-*/%^'

def is_whitespace(character):
    '''Checks if character is a whitespace.'''

    return character != '' and character in ' \n\t'

# TODO : Add support for constants
CONSTANTS = {
    'e': math.e,
    'pi': math.pi,
}

OPERATORS = {
    'infix':
    {
        '+': {
            'priority': 0,
            'function': operator.add
        },
        '-': {
            'priority': 0,
            'function': operator.sub
        },
        '*': {
            'priority': 1,
            'function': operator.mul
        },
        '/': {
            'priority': 1,
            'function': operator.truediv
        },
        '%': {
            'priority': 1,
            'function': operator.mod
        },
        '^': {
            'priority': 2,
            'function': operator.pow
        },
    },
    'prefix':
    {
        '-': {
            'priority': 3,
            'function': operator.neg
        },
        'abs': {
            'priority': 3,
            'function': operator.abs
        },
        'sqrt': {
            'priority': 3,
            'function': math.sqrt
        },
        'floor': {
            'priority': 3,
            'function': math.floor
        },
        'ceil': {
            'priority': 3,
            'function': math.ceil
        },
        'sin': {
            'priority': 3,
            'function': math.sin
        },
        'cos': {
            'priority': 3,
            'function': math.cos
        },
        'tan': {
            'priority': 3,
            'function': math.tan
        },
        'exp': {
            'priority': 3,
            'function': math.exp
        },
        'ln': {
            'priority': 3,
            'function': math.log
        },
        'log': {
            'priority': 3,
            'function': math.log10
        }
    },
    'postfix':
    {
        '!': {
            'priority': 3,
            'function': math.factorial
        },
        '%': {
            'priority': 3,
            'function': lambda x: x/100
        }
    }
}
