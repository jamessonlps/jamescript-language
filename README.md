# Jamescript Language

Welcome to Jamescript, a powerful and expressive programming language inspired by JavaScript. Jamescript combines simplicity with familiar syntax, making it easy for developers to write efficient and readable code. This README will provide you with an overview of the language's features, syntax, and examples to help you get started.

## 🚀 Features

- ✨ Simple mathematical operations
- 🔢 Support for integers and strings
- ⚖️ Conditional statements using if/else
- 🔄 Loops using while
- 🧱 Block-based code organization with braces
- 🎯 Support for traditional function declaration and arrow functions
- 🧩 Type system for integers and strings

## 🧰 Syntax

The syntax of Jamescript is similar to JavaScript, making it easy for developers familiar with JavaScript to transition to Jamescript. Below is an example of the EBNF (Extended Backus-Naur Form) for the Jamescript code:

```ebnf
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

## 🌟 Examples

Let's take a look at some examples to showcase the power and flexibility of Jamescript.

### Mathematical Operations

Jamescript supports basic mathematical operations such as addition, subtraction, multiplication, and division.

```ts
let x = 5 + 3; // x = 8
let y = x * 2; // y = 16
let z = y / 4; // z = 4
```

### Working with Integers and Strings

Jamescript allows you to work with both integers and strings seamlessly.

```ts
let number = 42;
let message = "Hello, world!";
```

## 📑 Presentation

- To access PDF document, [click here](/presentation/Linguagem.pdf).

- To access Power Point presentation, [click here](/presentation/Linguagem.pptx).

___

We hope you enjoy using Jamescript! If you have any questions, feedback, or suggestions, please don't hesitate to reach out. Happy coding!

Author: jamessonlps
