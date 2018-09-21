import unittest
from evaluator import Expression as Exp

class EvaluatorTests(unittest.TestCase):
    def test_spaces(self):
        e1 = Exp('1+1').eval()
        e2 = Exp('1 + 1').eval()
        e3 = Exp(' 1+1').eval()
        e4 = Exp('1+1 ').eval()

        self.assertEqual(e1, 2)
        self.assertEqual(e2, 2)
        self.assertEqual(e3, 2)
        self.assertEqual(e4, 2)
    
    def test_no_parentheses(self):
        e1 = Exp('1+2').eval()
        e2 = Exp('1+2*3').eval()
        e3 = Exp('1+2*3^4').eval()
        e4 = Exp('1+2*3^4%5').eval()

        self.assertEqual(e1, 1+2)
        self.assertEqual(e2, 1+2*3)
        self.assertEqual(e3, 1+2*3**4)
        self.assertEqual(e4, 1+2*3**4%5)

if __name__ == '__main__':
    unittest.main()