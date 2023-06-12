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
BLOCK = { STATEMENT } ;

STATEMENT = ( λ | ASSIGNMENT | STDOUT | WHILE | IF | FUNCTION_DEC | FUNCTION_ARROW_DEC | RETURN | FUNCTION_CALL ), "\n" ;

ASSIGNMENT = ( CREATING | SETTING ) ;

CREATING = "const", IDENTIFIER, ":", TYPE, [ "=", RELEXPRESSION ] ;

TYPE = "integer" | "string" ;

SETTING = IDENTIFIER, "=", RELEXPRESSION ;

STDOUT = "stdout", "(", [ RELEXPRESSION, { ",", RELEXPRESSION } ], ")" ;

WHILE = "(", RELEXPRESSION, ")", "{", BLOCK, "}" ;

IF = "(", RELEXPRESSION, ")", "{", BLOCK, "}", [ ELSE ] ;

ELSE = "else", "{", BLOCK, "}" ;

FUNCTION_ARROW_DEC = "const", IDENTIFIER, "=", "(", [FUNCTION_PARAMETER], ")", ":", TYPE, "=>", "{", BLOCK, "}";

FUNCTION_DEC = "def", IDENTIFIER, "(", [FUNCTION_PARAMETER], ")", ":", TYPE, "{", BLOCK, "}";

FUNCTION_PARAMETER = TYPE, IDENTIFIER, { ",", TYPE, IDENTIFIER };

RETURN = "return", RELEXPRESSION;

FUNCTION_CALL = IDENTIFIER, "(", [ RELEXPRESSION, { ",", RELEXPRESSION } ] ,")";

RELEXPRESSION = EXPRESSION, { ( "==" | ">" | "<" | ">=" | "<=" | "=>" | "." ), EXPRESSION }
EXPRESSION = TERM, { ("+" | "-" | "||"), TERM } ;
TERM = FACTOR, { ("*" | "/" | "&&"), FACTOR } ;
FACTOR = (("+" | "-" | "!"), FACTOR) | NUMBER | STRING | "(", RELEXPRESSION, ")" | IDENTIFIER, ["(", RELEXPR, {",", RELEXPR} ,")"] | ("input", "(", ")") ;

IDENTIFIER = LETTER, { LETTER | DIGIT | "_" } ;
NUMBER = DIGIT, { DIGIT } ;
LETTER = ( a | ... | z | A | ... | Z ) ;
DIGIT = ( 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 0 ) ;
```

## 🌟 Examples

Let's take a look at some examples to showcase the power and flexibility of Jamescript.

### Mathematical Operations

Jamescript supports basic mathematical operations such as addition, subtraction, multiplication, and division.

```ts
const x : integer = 5 + 3; // x = 8
const y : integer = x * 2; // y = 16
const z : integer = y / 4; // z = 4
```

### Working with Integers and Strings

Jamescript allows you to work with both integers and strings seamlessly.

```ts
const number : integer = 42;
const message : string = "Hello, world!";
```

### Working with conditionals

Jamescript supports basic conditional operations such as if/else, and allows you to create functions in two different ways. 

```ts
// Retorna o máximo de 2 elementos
def max(integer m, integer n) : integer {
  const max : integer

  if (m >= n) {
    max = m
  } else {
    max = n
  }

  return max
}

// Retorna o mínimo de 2 elementos
const min = (integer m, integer n) : integer => {
  const min : integer

  if (m <= n) {
    min = m
  } else {
    min = n
  }

  return min
}

const x : integer = 10
const y : integer = 20
const z : integer = 30

stdout("Máximo entre y e z:", max(y, z))
stdout("Mínimo entre x e y:", min(x, y))
```

### Working with loops

Jamescript allows you to work with `while` loops.

```ts
const x : integer = 1
const y : integer = 5

while (x < y) {
  x = x + 1
}

stdout("x =", x)
```

## 📑 Presentation

- To access PDF document, [click here](/presentation/Linguagem.pdf).

- To access Power Point presentation, [click here](/presentation/Linguagem.pptx).


## ▶️ Executing

In the [compiler](/compiler/) directory, write the code in a `teste.james` file and run the following command:

```shell
python ./main.py teste.james
```

Or, if you are using an unix system:

```shell
python3 ./main.py teste.james
```

___

We hope you enjoy using Jamescript! If you have any questions, feedback, or suggestions, please don't hesitate to reach out. Happy coding!

Author: [Me](https://www.linkedin.com/in/jamesson-leandro/)
