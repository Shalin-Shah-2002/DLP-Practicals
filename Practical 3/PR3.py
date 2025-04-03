import re
import sys

KEYWORDS = {
    "main",
    "auto",
    "break",
    "case",
    "char",
    "const",
    "continue",
    "default",
    "do",
    "double",
    "else",
    "enum",
    "extern",
    "float",
    "for",
    "goto",
    "if",
    "inline",
    "int",
    "long",
    "register",
    "restrict",
    "return",
    "short",
    "signed",
    "sizeof",
    "static",
    "struct",
    "switch",
    "typedef",
    "union",
    "unsigned",
    "void",
    "volatile",
    "while",
}

OPERATORS = {"+", "-", "*", "/", "=", "==", "!=", "<", ">", "<=", ">=", "&&", "||"}
PUNCTUATION = {";", ",", "{", "}", "(", ")", "[", "]", ":", "."}


TOKEN_PATTERN = re.compile(r"\b\w+\b|[+\-*/=;,{}():]|\".*?\"|'.*?'")
COMMENT_PATTERN = re.compile(r"//.*?$|/\*.*?\*/", re.DOTALL | re.MULTILINE)


def categorize_token(token):
    if token in KEYWORDS:
        return "Keyword"
    elif token in OPERATORS:
        return "Operator"
    elif token in PUNCTUATION:
        return "Punctuation"
    elif re.match(r"^\d+(\.\d+)?$", token):
        return "Constant"
    elif re.match(r"^\".*?\"|\'.*?\'$", token):
        return "String"
    elif re.match(r"\d+[A-Za-z]+", token):
        return "Lexical Error"
    else:
        return "Identifier"


def lexical_analyzer(file_path):
    try:
        with open(file_path, "r") as file:
            code = file.read()
    except FileNotFoundError:
        print(f"Error: Cannot read file '{file_path}'")
        return [], {}

    code = re.sub(COMMENT_PATTERN, "", code)

    tokens = TOKEN_PATTERN.findall(code)

    categorized_tokens = [(token, categorize_token(token)) for token in tokens]

    symbol_table = {
        token: category
        for token, category in categorized_tokens
        if category in {"Identifier"}
    }

    return categorized_tokens, symbol_table


if __name__ == "__main__":

    file_path = "example.c"
    tokens, symbol_table = lexical_analyzer(file_path)

    for token, category in tokens:
        if category != "Lexical Error":
            print(f"{category}: {token}")

    print("\nSymbol Table:")
    for symbol, category in symbol_table.items():

        print(f"{symbol}")

    errors = [token for token, category in tokens if category == "Lexical Error"]
    if errors:
        print("\nLexical Errors Found:")
        for error in errors:
            print(f"Invalid token: {error}")
