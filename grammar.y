%{
/* Incluindo bibliotecas */
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

/* tokens */
#include "tokens.h"

/* Variáveis globais */
extern int line_number;
extern char* yytext;
extern int yylex();
%}

/* Definição dos tokens */
%token <string_val> IDENTIFIER STRING
%token <float_val> FLOAT
%token CONST FUNCTION FUNCTION_PARAM IF ELSE WHILE STDOUT
%token PLUS MINUS TIMES DIVIDE EQ NE GT LT GE LE ASSIGN
%token LPAR RPAR LBRACE RBRACE LBRACKET RBRACKET SEMICOLON COMMA COLON DOT

/* Precedência dos operadores */
%left '+' '-'
%left '*' '/'
%nonassoc '<' '>' EQ NE GE LE

/* Gramática */
%%
program: /* empty */
       | program statement_or_function
       ;

statement_or_function: statement
                     | function_declaration
                     ;

statement: const_declaration SEMICOLON
         | expression SEMICOLON
         | if_statement
         | while_statement
         | stdout_statement
         ;

const_declaration: CONST IDENTIFIER ASSIGN expression
                  ;

if_statement: IF LPAR expression RPAR block %prec EQ
            | IF LPAR expression RPAR block ELSE block
            ;

while_statement: WHILE LPAR expression RPAR block
                ;

stdout_statement: STDOUT LPAR expression RPAR SEMICOLON
                ;

expression: simple_expression
          | simple_expression comparison_operator simple_expression
          ;

simple_expression: term
                 | simple_expression PLUS term
                 | simple_expression MINUS term
                 ;

term: factor
    | term TIMES factor
    | term DIVIDE factor
    ;

factor: IDENTIFIER
      | FLOAT
      | STRING
      | LPAR expression RPAR
      | function_call
      ;

function_declaration: FUNCTION IDENTIFIER COLON function_param_list LBRACE block RBRACE
                     ;

function_param_list: /* empty */
                   | function_param
                   | function_param_list COMMA function_param
                   ;

function_param: FUNCTION_PARAM IDENTIFIER
              ;

function_call: IDENTIFIER LPAR argument_list RPAR
             ;

argument_list: /* empty */
             | expression
             | argument_list COMMA expression
             ;

block: LBRACE statements RBRACE
     ;

statements: /* empty */
          | statement_or_function statements
          ;
%%