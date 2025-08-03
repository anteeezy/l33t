use std::env;
use std::fs;

mod lexer;
mod parser;
mod interpreter; 

fn main() {
    // get the input filename from command line
    let args: Vec<String> = env::args().collect(); 
    if args.len() != 2 {
        eprintln!("usage: l33t <file.l33t>"); 
        return; 
    }

    let filename = &args[1]; 
    let source = fs::read_to_string(filename)
        .expect("couldnt read source");

    println!("source code:\n{}\n", source);

    let tokens = lexer::lex(&source);
    println!("tokens: {:?}", tokens);

    let ast = parser::parse(&tokens);
    println!("ast: {:?}", ast);

    interpreter::run(&ast);
}
