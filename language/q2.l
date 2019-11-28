%{
    #include<stdio.h>
    int assign = 0;
    int relop = 0;
    int identifier = 0;
%}

%%
[a-zA-Z"_"][a-zA-Z"_"0-9]* {identifier++;}
%%
int yywrap(void) {}
int main(){
    extern FILE *yyin;
    yyin = fopen("input.c",'r');
    yylex();
    printf("%d %d %d\n",assign,relop,identifier);
    return 0;
}