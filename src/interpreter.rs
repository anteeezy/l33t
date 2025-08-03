use crate::parser::ASTNode;

pub fn run(ast: &[ASTNode]) {
    for node in ast {
        match node {
            ASTNode::Print(text) => println!("{}", text),
        }
    }
}
