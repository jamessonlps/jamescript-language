# jamescript-language

```
PROGRAM = { STATEMENT | FUNCTION } ;
CONST_DECLARATION = "const", IDENTIFIER, "=", EXPRESSION, ";" ;

FUNCTION_CALL = IDENTIFIER, "(", { EXPRESSION, { ",", EXPRESSION } }, ")" ;
FUNCTION = "function", IDENTIFIER, ":", FUNCTION_PARAM_LIST, "{", BLOCK, "}"
FUNCTION_PARAM_LIST = λ | FUNCTION_PARAM, { ",", FUNCTION_PARAM }
FUNCTION_PARAM = "param", IDENTIFIER ;

BLOCK = "{", { STATEMENT }, "}" ;
STATEMENT = ( EXPRESSION | STDOUT | IF_STATEMENT | WHILE_STATEMENT | CONST_DECLARATION ), ";" ;

IF_STATEMENT = "if", "(", EXPRESSION, ")", BLOCK, { "else", "(", BLOCK, ")" } ;
WHILE_STATEMENT = "while", "(", EXPRESSION, ")", BLOCK ;

STDOUT = "stdout", "(", EXPRESSION, ")" ;

EXPRESSION = SIMPLE_EXPRESSION | SIMPLE_EXPRESSION, COMPARISON_OPERATOR, SIMPLE_EXPRESSION ;
SIMPLE_EXPRESSION = TERM, { ("+" | "-"), TERM } ;
TERM = FACTOR, { ("*" | "/"), FACTOR } ;
FACTOR = IDENTIFIER | "(" EXPRESSION ")" | NUMBER | STRING | FUNCTION_CALL ;

IDENTIFIER = ( LETTER | "_" ), { LETTER | DIGIT | "_" } ;
STRING = '"', CHARACTER, { CHARACTER }, '"' ;
CHARACTER = ( LETTER | DIGIT | MATH_OPERATOR | CHARACTER ) ;
MATH_OPERATOR = ( "+" | "-" | "/" | "*" ) ;
COMPARISON_OPERATOR = "<" | "<=" | ">" | ">=" | "==" | "!=";
SYMBOL = ( "." | "_" | "@" | "#" | "!" | "&" | "(" | ")" | "{" | "}" | "[" | "]" ) ;
LETTER = ( a | ... | z | A | ... | Z ) ;
NUMBER = DIGIT, { DIGIT }, ( λ | ( ".", DIGIT, {DIGIT} ) );
DIGIT = ( 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 0 ) ;
```
