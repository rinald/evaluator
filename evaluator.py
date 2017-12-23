import sys
from helpers import *
from parenthesise import parenthesise

def evaluate(expression):
    expression = parse(expression)
    return expression.evaluate()

def main():
    running = True
    
    while running:
        expression = input('>>> ')

        if expression == 'quit':
            running = False
        else:
            print(parenthesise(expression))
    
    sys.exit(0)

if __name__ == '__main__':
    main()