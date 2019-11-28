%{
    #include <stdio.h>
%}

%token NUMBER;
%left '+' '-'
%left '*' '/' '%'
%left '(' ')'

%%
start:E {printf("Ans = %d\n",$$);}
E:E'+'E {$$ = $1 + $3;}
 |E'-'E {$$ = $1 - $3;}
 |NUMBER {$$ = $1;}
%%
int yyerror(){
    printf("Error\n");
}
int main(){
    yyparse();
    return 0;
}