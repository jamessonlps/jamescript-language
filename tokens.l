%{
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

/* Variável global */
int line_number = 1; /* Número da linha atual */
%}

/* Tokens */
%%

"const"             { return CONST; }
"function"          { return FUNCTION; }
"param"             { return FUNCTION_PARAM; }
"if"                { return IF; }
"else"              { return ELSE; }
"while"             { return WHILE; }
"stdout"            { return STDOUT; }
"+"                 { return PLUS; }
"-"                 { return MINUS; }
"*"                 { return TIMES; }
"/"                 { return DIVIDE; }
"=="                { return EQ; }
"!="                { return NE; }
">"                 { return GT; }
"<"                 { return LT; }
">="                { return GE; }
"<="                { return LE; }
"="                 { return ASSIGN; }
"("                 { return LPAR; }
")"                 { return RPAR; }
"{"                 { return LBRACE; }
"}"                 { return RBRACE; }
"["                 { return LBRACKET; }
"]"                 { return RBRACKET; }
";"                 { return SEMICOLON; }
","                 { return COMMA; }
":"                 { return COLON; }
"."                 { return DOT; }
"_"[a-zA-Z0-9_]*    { yylval.string_val = strdup(yytext); return IDENTIFIER; }
[0-9]+(\.[0-9]+)?   { yylval.float_val = atof(yytext); return FLOAT; }
\"(\\.|[^\"])*\"    { yylval.string_val = strdup(yytext+1); yylval.string_val[strlen(yylval.string_val)-1] = 0; return STRING; }
[\t ]+              { /* Ignora espaços em branco e tabs */ }
\n                  { line_number++; } /* Incrementa o número da linha */
.                   { printf("Erro: Invalid char '%c' in line %d.\n", yytext[0], line_number); exit(1); } /* Trata erros léxicos */

%%

int main(void) {
  yylex();
  return 0;
}
