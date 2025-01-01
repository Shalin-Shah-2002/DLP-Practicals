#include <iostream>
#include <string>
using namespace std;

bool simulateAutomaton(const string& input) {
    int currentState = 1;
    for (char c : input) {
        if (currentState == 1 && c == 'a') currentState = 2;
        else if (currentState == 1 && c == 'b') currentState = 3;
        else if (currentState == 2 && c == 'a') currentState = 1;
        else if (currentState == 2 && c == 'b') currentState = 4;
        else if (currentState == 3 && c == 'a') currentState = 4;
        else if (currentState == 3 && c == 'b') currentState = 1;
        else if (currentState == 4 && c == 'a') currentState = 3;
        else if (currentState == 4 && c == 'b') currentState = 2;
        else return false;
    }
    return currentState == 2;
}

int main() {
    string input;
    cout << "Enter the input string: ";
    cin >> input;

    if (simulateAutomaton(input))
        cout << "The input string is accepted\n";
    else
        cout << "The input string is rejected.\n";

    return 0;
}