class DFA:
    def __init__(
        self, num_states, input_symbols, start_state, final_states, transition_function
    ):
        self.num_states = num_states
        self.input_symbols = input_symbols
        self.start_state = start_state
        self.final_states = final_states
        self.transition_function = transition_function

    def is_accepting(self, input_string):
        current_state = self.start_state

        for symbol in input_string:
            if symbol not in self.input_symbols:
                return False

            current_state = self.transition_function.get((current_state, symbol))

            if current_state is None:
                return False

        return current_state in self.final_states


def main():
    # Test Case 0
    num_states = 4
    input_symbols = ["a", "b"]
    start_state = "q1"
    final_states = ["q4"]
    transition_function = {
        ("q1", "a"): "q2",
        ("q1", "b"): "q3",
        ("q2", "a"): "q1",
        ("q2", "b"): "q4",
        ("q3", "a"): "q4",
        ("q3", "b"): "q1",
        ("q4", "a"): "q3",
        ("q4", "b"): "q2",
    }
    test_strings = ["aba", "ab"]

    # Test Case 1
    # num_states = 5
    # input_symbols = ["1", "0"]
    # start_state = "A"
    # final_states = ["A", "D"]
    # transition_function = {
    #     ("A", "1"): "A",
    #     ("A", "0"): "B",
    #     ("B", "1"): "C",
    #     ("B", "0"): "E",
    #     ("C", "1"): "D",
    #     ("C", "0"): "E",
    #     ("D", "1"): "D",
    #     ("D", "0"): "B",
    #     ("E", "1"): "E",
    #     ("E", "0"): "E",
    # }
    # test_strings = ["011", "1"]

    dfa = DFA(num_states, input_symbols, start_state, final_states, transition_function)

    print("Testing DFA:")
    for test_string in test_strings:
        if dfa.is_accepting(test_string):
            print(f"String '{test_string}' is accepted.")
        else:
            print(f"String '{test_string}' is rejected.")


if __name__ == "__main__":
    main()
