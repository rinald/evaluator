"""Helper functions and structures."""

operator = {
    '+' : {
        "priority": 0,
    },
    '-' : {
        "priority": 0,
    },
    '*' : {
        "priority": 1,
    },
    '/' : {
        "priority": 1,
    },
}

def test(filename, function):
    with open(filename, mode='r') as file:
        lines = file.readlines()

        for line in lines:
            test_input, expected_output = line.split()
            test_output = function(test_input)
            assert test_output == expected_output

        print('Test was passed.')

def seperate(expression, operands, operators):
    """Seperate an expression into two lists, namely operands and operators.
    
    Arguments:
    expression -- a mathematical expression (e.g: 1+2*3-(1+2)/3)
    operands -- an empty list that will contain the operands of the expression
    operators -- an empty list that will contain the (infix) operators of the expression
    """
    pass

## TEMPORARY ##
def parenthesise(expression):
    """Return a fully parenthesised expression, equivalent to the one given.

    Arguments:
    expression -- a mathematical expression (e.g: 1+2*3-(1+2)/3)
    """
    pass

def parse(expression):
    pass