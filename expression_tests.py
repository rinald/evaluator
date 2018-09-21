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
        self.assertEqual(Exp(exp1).eval(), 1+2)
        self.assertEqual(Exp(exp2).eval(), 1+2-3)
        self.assertEqual(Exp(exp3).eval(), 1+2-3*4)
        self.assertEqual(Exp(exp4).eval(), 1+2-3*4**5)
        self.assertEqual(Exp(exp5).eval(), 1+2-3*4**5%6)

    def test_floats(self):
        exp1 = '1.0 + 2.0'
        exp2 = '1/5 + 4/5'
        exp3 = '2.1*2-0.2'
        exp4 = '1/5/5.0'
        self.assertEqual(Exp(exp1).eval(), 1.0+2.0)
        self.assertEqual(Exp(exp2).eval(), 1/5+4/5)
        self.assertEqual(Exp(exp3).eval(), 2.1*2-0.2)
        self.assertEqual(Exp(exp4).eval(), 1/5/5.0)

    def test_spaces(self):
        exp1 = '1 + 1'
        exp2 = ' 1+1'
        exp3 = '1+1 '
        self.assertEqual(Exp(exp1).eval(), 1+1)
        self.assertEqual(Exp(exp2).eval(), 1+1)
        self.assertEqual(Exp(exp3).eval(), 1+1)

    def test_parentheses(self):
        exp1 = '(1+2)*3'
        exp2 = '(1+2)*(3-4)'
        exp3 = '(0-1)^(1+1)'
        exp4 = '1/(1+2+3+4)'
        exp5 = '(((1)))'
        self.assertEqual(Exp(exp1).eval(), (1+2)*3)
        self.assertEqual(Exp(exp2).eval(), (1+2)*(3-4))
        self.assertEqual(Exp(exp3).eval(), (0-1)**(1+1))
        self.assertEqual(Exp(exp4).eval(), 1/(1+2+3+4))
        self.assertEqual(Exp(exp5).eval(), 1)

    def test_functions(self):
        exp1 = 'sin(0) + cos(0)'
        exp2 = 'ln(exp(3))'
        exp3 = 'log(2) + log(5)'
        exp4 = 'log(abs(0-10))'
        self.assertEqual(Exp(exp1).eval(), sin(0)+cos(0))
        self.assertEqual(Exp(exp2).eval(), log(exp(3)))
        self.assertEqual(Exp(exp3).eval(), exp(log(3)))
        self.assertEqual(Exp(exp4).eval(), log10(abs(0-10)))

if __name__ == '__main__':
    unittest.main()