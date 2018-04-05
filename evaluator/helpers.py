"""Defines helper functions and structures."""

import math
import operator

def is_digit(character):
    """Checks if character is a digit."""

    return character != "" and character in "0123456789"

def is_letter(character):
    """Checks if character is a (lowercase) letter."""

    return character != "" and character in "abcdefghijklmnopqrstuvwxyz"

def is_operator(character):
    """Checks if character is an operator."""

    return character != "" and character in "+-*/%^"

def is_whitespace(character):
    """Checks if character is a whitespace."""

    return character != "" and character in " \n\t"

OPERATORS = {
    # Arithmetic operators
    "+": {
        "priority": 0,
        "type": "infix",
        "function": operator.add
    },
    "-": {
        "priority": 0,
        "type": "infix",
        "function": operator.sub
    },
    "*": {
        "priority": 1,
        "type": "infix",
        "function": operator.mul
    },
    "/": {
        "priority": 1,
        "type": "infix",
        "function": operator.truediv
    },
    "%": {
        "priority": 2,
        "type": "infix",
        "function": operator.mod
    },
    "^": {
        "priority": 3,
        "type": "infix",
        "function": operator.pow
    },
    # Mathematical functions
    "abs": {
        "priority": 4,
        "type": "prefix",
        "function": abs
    },
    "floor": {
        "priority": 4,
        "type": "prefix",
        "function": math.floor
    },
    "ceil": {
        "priority": 4,
        "type": "prefix",
        "function": math.ceil
    },
    "sin": {
        "priority": 4,
        "type": "prefix",
        "function": math.sin
    },
    "cos": {
        "priority": 4,
        "type": "prefix",
        "function": math.cos
    },
    "tan": {
        "priority": 4,
        "type": "prefix",
        "function": math.tan
    },
    "exp": {
        "priority": 4,
        "type": "prefix",
        "function": math.exp
    },
    "log": {
        "priority": 4,
        "type": "prefix",
        "function": math.log
    },
}
