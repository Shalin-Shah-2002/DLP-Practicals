#include <stdio.h>
#include <string.h>
#include <stdbool.h>

bool regex_match(const char *str, const char *pattern) {
    int i = 0, j = 0;
    while (str[i] != '\0' && (str[i] == 'a' || str[i] == 'b')) {
        if (str[i] == 'b') {
            j++;
        }
        i++;
    }
    return (j == 2 && str[i] == '\0');
}

int main() {
    char input[100];

    printf("Enter a string: ");
    fgets(input, sizeof(input), stdin);
    input[strcspn(input, "\n")] = 0;
    if (regex_match(input, "^a*bb$")) {
        printf("Valid string\n");
    } else {
        printf("Invalid string\n");
    }
    return 0;
}
