import unittest
from evaluator.lexer import Lexer

class LexerTest(unittest.TestCase):
    def test_lexer(self):
        lexer = Lexer('1234567890 0.123456789 +-*/#^%! ([{<>}]) sin cos abs x y r theta e pi phi i')
        
        expected_type = {
            '1234567890': 'integer',
            '0.123456789': 'decimal',
            '+': 'operator',
            '-': 'operator',
            '*': 'operator',
            '/': 'operator',
            '^': 'operator',
            '#': 'operator',
            '%': 'operator',
            '!': 'operator',
            '(': 'left_round',
            ')': 'right_round',
            '[': 'left_square',
            ']': 'right_square',
            '{': 'left_curly',
            '}': 'right_curly',
            '<': 'left_angular',
            '>': 'right_angular',
            'sin': 'function',
            'cos': 'function',
            'abs': 'function',
            'x': 'variable',
            'y': 'variable',
            'r': 'variable',
            'theta': 'variable',
            'e': 'constant',
            'pi': 'constant',
            'phi': 'constant',
            'i': 'constant'
        }

        token = lexer.next()
        while token != None:
            self.assertEqual(token.type, expected_type[token.value])
            token = lexer.next()
        
if __name__ == '__main__':
    unittest.main()
