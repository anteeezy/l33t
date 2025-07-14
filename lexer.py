# print "hello world" -> 
#[
#    ('KEYWORD', 'print'),
#    ('STRING', 'hello world')
#]
import re

def lexer(source_code):
    print("lexing...")
    
    token_mapping = [
        ('KEYWORD', r'\bprint\b'),      # print keyword
        ('STRING', r'"([^"]*)"'),       # quoted string
        ('NEWLINE',  r'\n'),
        ('SKIP', r'[ \t]+'),            # skip spaces/tabs
        ('MISMATCH', r'.')              # any other character (error)
    ]
    
    # Combine all regex patterns into one pattern using named groups like (?P<KEYWORD>\bprint\b)|(?P<STRING>"[^"]*")|...
    token_regex = '|'.join(f'(?P<{name}>{pattern})' for name, pattern in token_mapping)
    
    tokens = [] # like [('KEYWORD', 'print')]
    line_num = 1
    
    for match in re.finditer(token_regex, source_code):
        kind = match.lastgroup          # name of the groupmatched like 'KEYWORD' or 'STRING
        print(kind)
        value = match.group()           # matched text like 'print' or 'hello
        print(value)
        
        if kind == 'NEWLINE':
            line_num += 1
        elif kind == 'SKIP':
            continue
        elif kind == 'STRING':
            strip = value[1:-1]
            tokens.append((kind, strip))
        elif kind == 'MISMATCH':
            raise SyntaxError(f"Unexpected character {value!r} on line {line_num}")
        else:
            tokens.append((kind, value))
        