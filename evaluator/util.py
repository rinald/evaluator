'''Defines utility functions and structures.'''

import math

MAX_BP = 4

is_digit      = lambda ch: ch != '' and ch in '0123456789'
is_letter     = lambda ch: ch != '' and ch in 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
is_operator   = lambda ch: ch != '' and ch in '+-*/#^%!'
is_bracket    = lambda ch: ch != '' and ch in '()[]{}<>'
is_whitespace = lambda ch: ch != '' and ch in ' \n\t'

CONSTANTS = {
    'e': math.e,
    'pi': math.pi,
    'i': 1j,
    'phi': (1 + math.sqrt(5)) / 2
}

OPERATORS = {
    'infix':
    {
        '+': {
            'bp': 1,
            'function': lambda x,y: x+y
        },
        '-': {
            'bp': 1,
            'function': lambda x,y: x-y
        },
        '*': {
            'bp': 2,
            'function': lambda x,y: x*y
        },
        '/': {
            'bp': 2,
            'function': lambda x,y: x/y
        },
        '#': {
            'bp': 2,
            'function': lambda x,y: x%y
        },
        '^': {
            'bp': 3,
            'function': lambda x,y: x**y
        },
    },
    'prefix':
    {
        '+': {
            'bp': 4,
            'function': lambda x: x
        },
        '-': {
            'bp': 4,
            'function': lambda x: -x
        },
        'abs': {
            'bp': 4,
            'function': lambda x: abs(x)
        },
        'sqrt': {
            'bp': 4,
            'function': lambda x: math.sqrt(x)
        },
        'floor': {
            'bp': 4,
            'function': lambda x: math.floor(x)
        },
        'ceil': {
            'bp': 4,
            'function': lambda x: math.ceil(x)
        },
        'sin': {
            'bp': 4,
            'function':lambda x: math.sin(x)
        },
        'cos': {
            'bp': 4,
            'function': lambda x: math.cos(x)
        },
        'tan': {
            'bp': 4,
            'function': lambda x: math.tan(x)
        },
        'exp': {
            'bp': 4,
            'function': lambda x: math.exp(x)
        },
        'ln': {
            'bp': 4,
            'function': lambda x: math.log(x)
        },
        'log': {
            'bp': 4,
            'function': lambda x: math.log10(x)
        }
    },
    'postfix':
    {
        '!': {
            'bp': 5,
            'function': lambda x: math.factorial(x)
        },
        '%': {
            'bp': 5,
            'function': lambda x: x/100
        }
    }
}
