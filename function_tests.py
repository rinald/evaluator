import unittest
from math import sin, cos, log, log10, exp, e, pi
from evaluator import Fun

class FunctionTest(unittest.TestCase):
    def test_x(self):
        f1 = Fun('(x-1)^2')
        self.assertEqual(f1(x=0), 1)
        self.assertEqual(f1(x=1), 0)
        self.assertEqual(f1(x=10), 81)
        f2 = Fun('-abs(x)')
        self.assertEqual(f2(x=0), 0)
        self.assertEqual(f2(x=3), -3)
        self.assertEqual(f2(x=-3), -3)
    def test_xy(self):
        f1 = Fun('x/y')
        self.assertEqual(f1(x=0, y=1), 0)
        self.assertEqual(f1(x=1, y=10), 0.1)
        self.assertEqual(f1(x=123, y=123), 1)
        f2 = Fun('ln(x) + ln(y)')
        self.assertEqual(f2(x=e, y=e), 2)
        self.assertEqual(f2(x=1, y=1), 0)
        self.assertEqual(f2(x=1, y=e), 1)
    def test_xyz(self):
        f1 = Fun('1/x+1/y+1/z')
        self.assertEqual(f1(x=1, y=1, z=1), 3)
        self.assertEqual(f1(x=1, y=2, z=3), 1+1/2+1/3)
        self.assertEqual(f1(x=-1, y=15, z=-15), -1)
        f2 = Fun('sin(x) + cos(y) + tan(z)')
        self.assertEqual(f2(x=0, y=0, z=0), 1)
        self.assertEqual(f2(x=pi, y=pi, z=pi), -1)
        self.assertEqual(f2(x=0, y=2*pi, z=0), 1)
        
    
if __name__ == '__main__':
    unittest.main()