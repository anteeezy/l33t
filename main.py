import sys

# Placeholder lexer
def tokenize(source_code):
    print("Lexing...")
    tokens = source_code.split()  # Dummy lexer splits by spaces
    return tokens

# Placeholder parser
def parse(tokens):
    print("Parsing...")
    ast = tokens  # Dummy parser just passes tokens as AST
    return ast

# Placeholder interpreter
def evaluate(ast):
    print("Interpreting...")
    # For now, just print the AST contents
    return ' '.join(ast)
    
def run_l33tlang(filename):
    # open file and read it
    with open(filename, 'r') as f:
        source_code = f.read()

    try: 
        tokens = tokenize(source_code)
        ast = parse(tokens)
        result = evaluate(ast)
        print(result)
    except Exception as e:
        print(f"[error] {e}")
        
if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <file.l33t>")
        sys.exit(1)

    run_l33tlang(sys.argv[1])
