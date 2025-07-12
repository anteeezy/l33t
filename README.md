# L33tLang

A simple programming language built in Python with a l33t aesthetic!

## Features

- Basic arithmetic operations
- Variable assignment and usage
- Print statements
- Simple control flow
- L33t-style syntax

## Example Usage

```
// Basic arithmetic
x = 5 + 3
y = x * 2
print y

// L33t-style variables
h4x0r = "Hello World!"
print h4x0r
```

## How to Run

```bash
python l33tlang.py your_script.l33t
```

## Language Structure

l33tLang uses a simple syntax:
- Variables: `variable_name = value`
- Print: `print expression`
- Numbers: `123`, `3.14`
- Strings: `"hello world"`
- Operations: `+`, `-`, `*`, `/`

## Architecture

- **Lexer**: Tokenizes source code
- **Parser**: Creates Abstract Syntax Tree
- **Interpreter**: Executes the AST

l33tlang/
├── __init__.py
├── main.py                # Entry point: CLI or REPL
├── lexer.py               # Tokenizer: converts code → tokens
├── parser.py              # Builds AST from tokens
├── ast_nodes.py           # Classes for AST node types
├── interpreter.py         # Walks AST, executes code (if interpreted)
├── compiler.py            # (Optional) Converts AST to bytecode, C, etc.
├── errors.py              # Custom exceptions & error handling
├── tokens.py              # Token types and constants
├── environment.py         # Variable scopes, symbol table
├── stdlib/                # Built-in functions, modules, etc.
│   └── __init__.py
├── tests/                 # Unit tests for lexer/parser/etc.
│   └── test_lexer.py
└── examples/              # Sample `.leet` files to run
    └── hello.leet

