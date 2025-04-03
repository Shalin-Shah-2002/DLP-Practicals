class RecursiveDescentParser:
    def __init__(self, input_text):
        self.tokens = list(input_text)  
        self.current_token_index = 0

    def peek(self):
        if self.current_token_index < len(self.tokens):
            return self.tokens[self.current_token_index]
        return None

    def consume(self):
        token = self.peek()
        self.current_token_index += 1
        return token

    def S(self):
        token = self.peek()
        
        if token == 'a':  
            self.consume()
            return True
        elif token == '(':  
            self.consume()  
            if self.L():
                if self.consume() == ')':  
                    return True
                else:
                    raise SyntaxError("Expected ')'")
            else:
                raise SyntaxError("Invalid L inside '( )'")
        else:
            return False  

    def L(self):
        """Handles the rule: L → S L’"""
        if self.S():
            return self.L_prime()
        return False

    def L_prime(self):
        """Handles the rule: L’ → , S L’ | ϵ (empty)"""
        if self.peek() == ',':  
            self.consume()  
            if self.S():
                return self.L_prime()  
            else:
                raise SyntaxError("Expected 'S' after ','")
        return True 

    def parse(self):
        """Starts parsing and ensures the entire input is consumed."""
        if self.S() and self.peek() is None:
            return "Valid String"
        else:
            raise SyntaxError("Unexpected characters at end of input")


if __name__ == "__main__":
    test_strings = [
        "a",          # Valid (S → a)
        "(a)",        # Valid (S → ( L ) where L → S)
        "(a,a)",      # Valid (S → ( L ) where L → S, S)
        "(a,a,a)",    # Valid (S → ( L ) where L → S, S, S)
        "()",         # Invalid (Empty L)
        "(a,)",       # Invalid (Comma without another S)
        "(a,(a,a))",  # Valid (Nested expressions)
        "(a,a,a",     # Invalid (Missing ')')
        "a,a",        # Invalid (No outer parentheses)
    ]

    for expr in test_strings:
        try:
            parser = RecursiveDescentParser(expr)
            result = parser.parse()
            print(f"Input: {expr} → {result}")
        except SyntaxError as e:
            print(f"Input: {expr} → Invalid: {e}")
