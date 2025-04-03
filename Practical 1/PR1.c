#include <stdio.h>
#include <string.h>

int check(char *reg)
{
    int n = strlen(reg);

    if (n == 2)
    {
        return 0;
    }

    // if (n == 2 && reg[n - 1] == 'b' && reg[n] == 'b')
    // {
    //     return 0;
    // }

    if (n < 2)
    {
        return 0;
    }

    if (reg[n - 2] != 'b' || reg[n - 1] != 'b')
    {
        return 0;
    }

    for (int i = 0; i < n - 2; i++)
    {
        if (reg[i] != 'a')
        {
            return 0;
        }
    }

    return 1;
}

int main()
{
    char input[7];
    int s;
    printf("Enter a string: ");
    scanf("%s", input);

    if (check(input))
    {
        printf("Valid string\n");
    }
    else
    {
        printf("Invalid string\n");
    }
    return 0;
}
