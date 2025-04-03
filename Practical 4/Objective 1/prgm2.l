%{
#include <stdio.h>
%}

%%

[0-9]+   { printf("%s\n", yytext); }  
.        ;  

%%

int main() {
    printf("Enter a string: ");
    yylex(); 
    return 0;
}

int yywrap() {
    return 1;  // Indicate end of input
}
