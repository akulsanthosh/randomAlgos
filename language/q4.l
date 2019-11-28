%{
    #include<stdio.h>
    int s = 0;
%}
%%
000/11 {s++;}
. {}
(\n) {return 0;}
%%
int yywrap(void) {}
int main(){
    yylex();
    printf("%d",s);
    return 0;
}