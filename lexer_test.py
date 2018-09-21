from evaluator.lexer import Lexer

def main():
    lexer = Lexer('1+1-1*1/1%1^1 + (1+1-1*1/1%1^1) + sin(1) + cos(1) + tan(1) + ln(1) + log(1) + exp(1)')
    
    for token in lexer:
        print(token)
        
if __name__ == '__main__':
    main()

