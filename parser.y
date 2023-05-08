%{
  /* Definitions */
  #include<stdio.h>
  int yylex();
  void yyerror(const char *s) { printf("ERROR:  %s\n", s); }
%}

%token LEFT_PARENTHESIS
%token RIGHT_PARENTHESIS
%token LEFT_BRACE
%token RIGHT_BRACE
%token NUMBER
%token STRING
%token COLON

%token CONST
%token STDOUT
%token IDENTIFIER
%token FUNCTION
%token FUNCTION_IDENTIFIER
%token PARAM

%token IF
%token ELSE
%token WHILE

%token MULTIPLY
%token DIVIDE
%token PLUS
%token MINUS
%token ASSIGN
%token SEMICOLON
%token COMMA

%token AND
%token OR
%token GT
%token LT
%token GTE
%token LTE
%token EQ

%start program

%%

factor: NUMBER
| STRING
| IDENTIFIER
| LEFT_PARENTHESIS rel_expression RIGHT_PARENTHESIS
| function_call
;

term: factor
| factor MULTIPLY factor
| factor DIVIDE factor
| factor AND factor
;

expression: term
| term PLUS term
| term MINUS term
| term OR term
;

rel_expression: expression
| expression GT expression
| expression LT expression
| expression GTE expression
| expression LTE expression
| expression EQ expression
;

function_call_params: rel_expression
| rel_expression COMMA rel_expression
;

function_call: FUNCTION_IDENTIFIER LEFT_PARENTHESIS RIGHT_PARENTHESIS
| FUNCTION_IDENTIFIER LEFT_PARENTHESIS function_call_params RIGHT_PARENTHESIS
;

function_param: PARAM FUNCTION_IDENTIFIER;

function_param_list: /* empty */
| function_param
| function_param_list COMMA function_param
;

function: FUNCTION FUNCTION_IDENTIFIER COLON function_param_list LEFT_BRACE block RIGHT_BRACE;

else_statement: /* empty */
| ELSE block
;

if_statement: IF LEFT_PARENTHESIS rel_expression RIGHT_PARENTHESIS block else_statement;

while_statement: WHILE LEFT_PARENTHESIS rel_expression RIGHT_PARENTHESIS block;

statement: function_call SEMICOLON
| CONST IDENTIFIER ASSIGN rel_expression SEMICOLON
| IDENTIFIER ASSIGN rel_expression SEMICOLON
| if_statement
| while_statement
| STDOUT LEFT_PARENTHESIS rel_expression RIGHT_PARENTHESIS SEMICOLON
;

block: LEFT_BRACE RIGHT_BRACE
| LEFT_BRACE statement RIGHT_BRACE
;

program: /* empty */
| program function
| program statement
;


%%

int main(){
  yyparse();
  return 0;
}
