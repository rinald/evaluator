# Evaluator
A simple evaluator for mathematical expressions.

The **evaluator** module provides two external objects: **Expression** and **Function**.

The **Expression** object represent a mathematical expression. It supports expressions with integers, operators and parentheses.
For negative integers you have to write **(0-i)** where **i** is a positive integer.
Support for embedded functions, prefix and postfix operators will be added later.

The **Function** object represents a one-variable mathematical function. It essentially is just an expression with variable **x**.
It is a callable object, so you can call it just like an ordinary function.

Example usage:

```python
from evaluator import Expression, Function

e = Expression('(1+2)*(3+4)-(((5)))') # Creates Expression object
print(e.evaluate()) # Evaluates the expression and prints it to stdout
e.reset('2^10 % 365') # Reset the expression

f = Function('x^2+2*x+1') # Creates Function object
print(f(-1)) # Prints 0
print(f.evaluate(-1)) # Same as previous line
f.reset('(x+1)/(x-1) + (x-1)/(x+1)')

```
