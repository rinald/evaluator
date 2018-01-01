import sys
from evaluator.simple_expression import SimpleExpression
from evaluator.operation import Operation

def main():
    expression = SimpleExpression("1+1-1*1/1^1%1")
    print(expression)

if __name__ == "__main__":
    sys.exit(main())
