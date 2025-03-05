import re

keywords = {'int', 'char', 'return', 'void', 'main', 'if', 'else', 'while', 'for'}
operators = {'+', '-', '*', '/', '=', '<', '>', '<=', '>=', '==', '!='}
punctuation = {'(', ')', '{', '}', ';', ',', '[', ']'}

token_specs = [
    ('NUMBER', r'\d+'),                         
    ('IDENTIFIER', r'[a-zA-Z_][a-zA-Z0-9_]*'),  
    ('OPERATOR', r'[\+\-\*/=<>!]+'),            
    ('PUNCTUATION', r'[(){}\[\];,]'),          
    ('STRING', r'"[^"]*"'),                      
    ('CHAR', r"'[^']'"),                       
    ('COMMENT', r'//.*|/\*.*?\*/'),              
    ('WHITESPACE', r'\s+'),                      
    ('INVALID', r'.'),                           
]


token_regex = '|'.join(f'(?P<{name}>{pattern})' for name, pattern in token_specs)

def lexical_analyzer(code):
    tokens = []
    for match in re.finditer(token_regex, code):
        token_type = match.lastgroup
        token_value = match.group(token_type)

        if token_type == 'WHITESPACE' or token_type == 'COMMENT':
            continue  # Ignore whitespace and comments
        elif token_type == 'NUMBER':
            tokens.append(('CONSTANT', token_value))
        elif token_type == 'IDENTIFIER':
            if token_value in keywords:
                tokens.append(('KEYWORD', token_value))
            else:
                tokens.append(('IDENTIFIER', token_value))
        elif token_type == 'OPERATOR':
            tokens.append(('OPERATOR', token_value))
        elif token_type == 'PUNCTUATION':
            tokens.append(('PUNCTUATION', token_value))
        elif token_type == 'STRING':
            tokens.append(('STRING', token_value))
        elif token_type == 'CHAR':
            tokens.append(('CHAR', token_value))
        elif token_type == 'INVALID':
            tokens.append(('INVALID', token_value))

    return tokens

code = """
int main() {
    int a = 5, 7H;
    char b = 'x';
    return a + b;
}
"""

tokens = lexical_analyzer(code)
for token in tokens:
    print(token)