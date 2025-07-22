import re

def lexer(source_code):
    print("lexing...")
    
    token_mapping = [
        ('KEYWORD', r'\bprint\b'),      # print keyword
        ('LET', r'blet\b'),             # let variable
        ('STRING', r'"[^"\n]*"'),       # quoted string
        ('IDENTIFIER', r'[A-Za-z_][A-Za-z0-9_]*'),  # identify 
        ('EQUALS', r'='),
        ('NEWLINE',  r'\n'),            # new line
        ('COMMENT', r'//.*'),           # support comments
        ('SKIP', r'[ \t]+'),            # skipspaces/tabs
        ('MISMATCH', r'.'),             # any other character (error)
    ]
    
    # Combine all regex patterns into one pattern using named groups like (?P<KEYWORD>\bprint\b)|(?P<STRING>"[^"]*")|...
    token_regex = '|'.join(f'(?P<{name}>{pattern})' for name, pattern in token_mapping)
    tokens = [] # like [('KEYWORD', 'print')]
    line_num = 1
    
    for match in re.finditer(token_regex, source_code):
        kind = match.lastgroup          # name of the groupmatched like 'KEYWORD' or 'STRING
        value = match.group()           # matched text like 'print' or 'hello
    
        if kind == 'NEWLINE':
            line_num += 1 
        elif kind == 'SKIP' or kind == 'COMMENT':
            continue
        elif kind == 'STRING':
            if value is not None and len(value) >= 2:
                strip = value[1:-1]
            else:
                strip = ''
            tokens.append((kind, strip))
        elif kind == 'MISMATCH':
            raise SyntaxError(f"Unexpected character {value!r} on line {line_num}")
        else: 
            tokens.append((kind, value))
    return tokens
