# Evaluator
A simple evaluator for mathematical expressions.

The **evaluator** package reexports the two main objects: **Expression** and **Function**.

The **Expression** object represent a mathematical expression. It supports expressions with numbers, constants, operators, parentheses and also embedded mathematical functions.

### Example usage:
```python
from evaluator import Exp

e = Exp('(1+2)*3-4')
print(e.eval()) # Prints 5

e = Exp('sin(1-ln(e))')
print(e.eval()) # Prints 0
```

---

The **Function** object represents a multivariable mathematical function. It essentially is just an expression with variables. It is a callable object, so you can call it just like an ordinary function.

### Example usage:

```python
from evaluator import Fun

## Single variable function
f = Fun('x^2+2*x+1')
print(f(x=-1)) # Prints 0

f = Fun('cos(theta)') # 'theta' is the variable in this case
print(f(theta=0)) # Prints 1

## Multivariable function
f = Fun('x+y')
print(f(x=1, y=2)) # Prints 3
print(f(x=1, z=2)) # Error

```

_For a list of operators, constants and functions, see **evaluator/util.py**_
