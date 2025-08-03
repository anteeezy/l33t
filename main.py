import sys

import lexer
import parser
import interpreter

def tokenize(source_code):
    tokens = lexer.lexer(source_code)
    print(tokens)
    return tokens

def parse(tokens):
    print("parsing...")
    ast = parser.parser(tokens)
    print(ast)
    return ast

def evaluate(ast):
    interpreter.interpreter(ast)

def run_l33tlang(filename):
    # open file and read it
    with open(filename, 'r') as f:
        source_code = f.read()

    try: 
        tokens = tokenize(source_code)
        ast = parse(tokens)
        result = evaluate(ast)

    except Exception as e:
        print(f"[error] {e}")
        
if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <file.l33t>")
        sys.exit(1)

    run_l33tlang(sys.argv[1])
