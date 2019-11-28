%{
    #include<stdio.h>
    #include<stdlib.h>
    int w = 0,c = 0,s = 0;
%}
%%
[^ \t\n]* {w++; c+=yyleng;}
(\n) {s++;}
%%
int yywrap(void) {}
int main(){
    extern FILE *yyin;
    yyin = fopen("input.txt","r");
    yylex();
    printf("words = %d\ncharactors = %d\nline = %d\n",w,c,s);
    return 0;
}