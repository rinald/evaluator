import unittest
from math import sin, cos, log, log10, exp
from evaluator import Expression as Exp

class ExpressionTest(unittest.TestCase):
    def test_no_parentheses(self):
        exp1 = '1+2'
        exp2 = '1+2-3'
        exp3 = '1+2-3*4'
        exp4 = '1+2-3*4^5'
        exp5 = '1+2-3*4^5%6'
        self.assertEqual(Exp(exp1).eval(), eval(exp1))
        self.assertEqual(Exp(exp2).eval(), eval(exp2))
        self.assertEqual(Exp(exp3).eval(), eval(exp3))
        self.assertEqual(Exp(exp4).eval(), eval(exp4.replace('^', '**')))
        self.assertEqual(Exp(exp5).eval(), eval(exp5.replace('^', '**')))

    def test_floats(self):
        exp1 = '1.0 + 2.0'
        exp2 = '1/5 + 4/5'
        exp3 = '2.1*2-0.2'
        exp4 = '1/5/5.0'
        self.assertEqual(Exp(exp1).eval(), eval(exp1))
        self.assertEqual(Exp(exp2).eval(), eval(exp2))
        self.assertEqual(Exp(exp3).eval(), eval(exp3))
        self.assertEqual(Exp(exp4).eval(), eval(exp4))

    def test_spaces(self):
        exp1 = '1 + 1'
        exp2 = ' 1+1'
        exp3 = '1+1 '
        self.assertEqual(Exp(exp1).eval(), eval(exp1))
        self.assertEqual(Exp(exp2).eval(), eval(exp2))
        self.assertEqual(Exp(exp3).eval(), eval(exp3))

    def test_parentheses(self):
        exp1 = '(1+2)*3'
        exp2 = '(1+2)*(3-4)'
        exp3 = '(0-1)^(1+1)'
        exp4 = '1/(1+2+3+4)'
        exp5 = '(((1)))'
        self.assertEqual(Exp(exp1).eval(), eval(exp1))
        self.assertEqual(Exp(exp2).eval(), eval(exp2))
        self.assertEqual(Exp(exp3).eval(), eval(exp3.replace('^', '**')))
        self.assertEqual(Exp(exp4).eval(), eval(exp4))
        self.assertEqual(Exp(exp5).eval(), eval(exp5))

    def test_functions(self):
        exp1 = 'sin(0) + cos(0)'
        exp2 = 'ln(exp(3))'
        exp3 = 'exp(ln(3))'
        exp4 = 'log(2) + log(5)'
        exp5 = 'log(abs(0-10))'
        self.assertEqual(Exp(exp1).eval(), eval(exp1))
        self.assertEqual(Exp(exp2).eval(), eval(exp2.replace('ln', 'log')))
        self.assertEqual(Exp(exp3).eval(), eval(exp3.replace('ln', 'log')))
        self.assertEqual(Exp(exp4).eval(), eval(exp4.replace('log', 'log10')))
        self.assertEqual(Exp(exp5).eval(), eval(exp5.replace('log', 'log10')))

if __name__ == '__main__':
    unittest.main()