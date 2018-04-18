# Evaluator
A simple evaluator for mathematical expressions.

The **evaluator** module provides two external objects: **Expression** and **Function**.

The **Expression** object represent a mathematical expression. It supports expressions with numbers, operators, parentheses and also embedded mathematical functions. For negative numbers you have to write **(0-i)** where **i** is a positive number.

The **Function** object represents a one-variable mathematical function. It essentially is just an expression with variable **x**.
It is a callable object, so you can call it just like an ordinary function.

_For a list of operators and functions, see **evaluator/helpers.py**_

## Example usage:

```python
from evaluator import Expression, Function

e = Expression("(1+2)*(3+4)-(((5)))") # Creates Expression object
print(e.eval()) # Evaluates the expression and prints it to stdout
e.reset("2^10 % 365") # Reset the expression

f = Function('x^2+2*x+1') # Creates Function object
print(f(-1)) # Prints 0
print(f.eval(-1)) # Same as previous line
f.reset("log(abs(x))")

```

