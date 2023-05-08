%{
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

/* Tokens */
#include "y.tab.h"

/* Variáv el global */
int line_number = 1; /* Número da linha atual */
%}

/* Tokens */
%%

"const"             { return CONST; }
"function"          { return FUNCTION; }
"param"             { return PARAM; }
"if"                { return IF; }
"else"              { return ELSE; }
"while"             { return WHILE; }
"stdout"            { return STDOUT; }
"+"                 { return PLUS; }
"-"                 { return MINUS; }
"*"                 { return MULTIPLY; }
"/"                 { return DIVIDE; }
"=="                { return EQ; }
">"                 { return GT; }
"<"                 { return LT; }
">="                { return GTE; }
"<="                { return LTE; }
"="                 { return ASSIGN; }
"("                 { return LEFT_PARENTHESIS; }
")"                 { return RIGHT_PARENTHESIS; }
"{"                 { return LEFT_BRACE; }
"}"                 { return RIGHT_BRACE; }
";"                 { return SEMICOLON; }
","                 { return COMMA; }
":"                 { return COLON; }

[a-zA-Z0-9_][a-zA-Z0-9_]+ { return IDENTIFIER; }
[0-9]+(\.[0-9]+)?         { return NUMBER; }
[\t]+                     { /* Ignora tabs */ }
\n                        { line_number++; } /* Incrementa o número da linha */

.  { printf("Erro: Invalid char '%c' in line %d.\n", yytext[0], line_number); exit(1); } /* Trata erros léxicos */


%%

int yywrap(void) {
  return 1;
}

