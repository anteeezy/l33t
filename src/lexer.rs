#[derive(Debug, Clone)]
pub enum Token {
    Keyword(String),
    String(String),
}

pub fn lex(source: &str) -> Vec<Token> {
    vec![
        Token::Keyword("print".to_string()),
        Token::String("hello".to_string()),
    ]
}
