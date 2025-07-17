# this will turn tokens from [('KEYWORD', 'print')] to {'type': 'print_statement'} 

def parser(tokens):
    ast = []
    i = 0

    while i < len(tokens):
        kind, value = tokens[i]

        if kind == 'KEYWORD' and value == 'print':
            if i + 1 < len(tokens) and tokens[i + 1][0] == 'STRING':
                ast.append({
                    "type": "print_statement",
                    "value": tokens[i + 1][1]
                })
                i += 2
            else:
                raise SyntaxError(f"[parser error] Expected STRING after print, got {tokens[i + 1]}")
        else:
            raise SyntaxError(f"[parser error] Unexpected token {tokens[i]}")
    return ast
