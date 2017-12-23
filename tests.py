"""Tests of helper functions and structures."""

import helpers
import parenthesise

def parenthesise_test():
    filename = 'parenthesise-tests.txt'
    function = parenthesise.parenthesise
    helpers.test(filename, function)