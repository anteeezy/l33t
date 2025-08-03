use crate::lexer::Token;

#[derive(Debug)]
pub enum ASTNode {
    Print(String),
}

// parse will take slices of tokens and return a vector of ast nodes
pub fn parse(tokens: &[Token]) -> Vec<ASTNode> {
    vec![ASTNode::Print("hello".to_string())]
}
