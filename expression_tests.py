import unittest
from math import sin, cos, log, log10, exp, e, pi
from evaluator import Exp

class ExpressionTest(unittest.TestCase):
    def test_no_parentheses(self):
        self.assertEqual(Exp('1+2').eval(), 1+2)
        self.assertEqual(Exp('1+2-3').eval(), 1+2-3)
        self.assertEqual(Exp('1+2-3*4').eval(), 1+2-3*4)
        self.assertEqual(Exp('1+2-3*4^5').eval(), 1+2-3*4**5)
        self.assertEqual(Exp('1+2-3*4^5#6').eval(), 1+2-3*4**5%6)

    def test_floats(self):
        self.assertEqual(Exp('1.0+2.0').eval(), 1.0+2.0)
        self.assertEqual(Exp('1/5+4/5').eval(), 1/5+4/5)
        self.assertEqual(Exp('2.1*2-0.2').eval(), 2.1*2-0.2)
        self.assertEqual(Exp('1/5/5.0').eval(), 1/5/5.0)

    def test_spaces(self):
        self.assertEqual(Exp('1 + 1').eval(), 1+1)
        self.assertEqual(Exp(' 1+1').eval(), 1+1)
        self.assertEqual(Exp('1+1 ').eval(), 1+1)

    def test_parentheses(self):
        self.assertEqual(Exp('(1+2)*3').eval(), (1+2)*3)
        self.assertEqual(Exp('(1+2)*(3-4)').eval(), (1+2)*(3-4))
        self.assertEqual(Exp('(0-1)^(1+1)').eval(), (0-1)**(1+1))
        self.assertEqual(Exp('1/(1+2+3+4)').eval(), 1/(1+2+3+4))

    def test_functions(self):
        self.assertEqual(Exp('sin(0)+cos(0)').eval(), sin(0)+cos(0))
        self.assertEqual(Exp('ln(exp(1))').eval(), log(exp(1)))
        self.assertEqual(Exp('exp(ln(1))').eval(), exp(log(1)))
        self.assertEqual(Exp('log(abs(0-10))').eval(), log10(abs(0-10)))
    
    def test_prefix(self):
        self.assertEqual(Exp('-1+1').eval(), -1+1)
        self.assertEqual(Exp('(-1)^(-1)').eval(), (-1)**(-1))
        self.assertEqual(Exp('(10^2)^(-1)').eval(), (10**2)**(-1))
        self.assertEqual(Exp('-(-1)').eval(), -(-1))
    
    def test_constants(self):
        self.assertEqual(Exp('e').eval(), e)
        self.assertEqual(Exp('pi').eval(), pi)
        self.assertEqual(Exp('ln(e^2)').eval(), log(e**2))
        self.assertEqual(Exp('e^(ln(pi))').eval(), e**log(pi))

if __name__ == '__main__':
    unittest.main()