"""Defines helper functions and structures."""

import math
import operator

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
    }
    
    # Mathematical functions
    # Implemented as prefix operators
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
} 