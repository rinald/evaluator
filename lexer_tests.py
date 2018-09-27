import unittest
from evaluator.lexer import Lexer

class LexerTest(unittest.TestCase):
    def test_lexer(self):
        lexer = Lexer('1 0.0 +- */ ^%! ([{<>}]) sin x pi')
        
        expected_type = {
            '1': 'integer',
            '0.0': 'decimal',
            '+': 'operator',
            '-': 'operator',
            '*': 'operator',
            '/': 'operator',
            '^': 'operator',
            '%': 'operator',
            '!': 'operator',
            '(': 'left_parenthesis',
            ')': 'right_parenthesis',
            '[': 'left_bracket',
            ']': 'right_bracket',
            '{': 'left_brace',
            '}': 'right_brace',
            '<': 'left_angular',
            '>': 'right_angular',
            'sin': 'function',
            'x': 'variable',
            'pi': 'constant'
        }

        token = lexer.next()
        while token != None:
            self.assertEqual(token.type, expected_type[token.value])
            token = lexer.next()
        
if __name__ == '__main__':
    unittest.main()
