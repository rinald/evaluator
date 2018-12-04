# Evaluator
A simple evaluator for mathematical expressions.

The **evaluator** package reexports the two main objects: **Expression** and **Function**.

The **Expression** object represent a mathematical expression. It supports expressions with numbers, constants, operators, parentheses and also embedded mathematical functions.

### Example usage:
```python
from evaluator import Exp

e = Exp('(1+2)*3-4')
print(e.eval()) # prints 5

e = Exp('sin(1-ln(e))')
print(e.eval()) # prints 0
```

---

The **Function** object represents a multivariable mathematical function. It essentially is just an expression with variables. It is a callable object, so you can call it just like an ordinary function.

### Example usage:

```python
from evaluator import Fun

## Single variable function
f = Fun('x^2+2*x+1')
print(f(x=-1)) # prints 0

f = Fun('cos(theta)') # 'theta' is the variable in this case
print(f(0)) # prints 1

## Multivariable function
f = Fun('x+y')
print(1, 2) # prints 3
print(f(x=1, y=2)) # same as above
print(f(x=1, z=2)) # error

```

_For a list of operators, constants and functions, see **evaluator/util.py**_
