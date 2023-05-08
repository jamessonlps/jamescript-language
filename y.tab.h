/* A Bison parser, made by GNU Bison 3.8.2.  */

/* Bison interface for Yacc-like parsers in C

   Copyright (C) 1984, 1989-1990, 2000-2015, 2018-2021 Free Software Foundation,
   Inc.

   This program is free software: you can redistribute it and/or modify
   it under the terms of the GNU General Public License as published by
   the Free Software Foundation, either version 3 of the License, or
   (at your option) any later version.

   This program is distributed in the hope that it will be useful,
   but WITHOUT ANY WARRANTY; without even the implied warranty of
   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
   GNU General Public License for more details.

   You should have received a copy of the GNU General Public License
   along with this program.  If not, see <https://www.gnu.org/licenses/>.  */

/* As a special exception, you may create a larger work that contains
   part or all of the Bison parser skeleton and distribute that work
   under terms of your choice, so long as that work isn't itself a
   parser generator using the skeleton or a modified version thereof
   as a parser skeleton.  Alternatively, if you modify or redistribute
   the parser skeleton itself, you may (at your option) remove this
   special exception, which will cause the skeleton and the resulting
   Bison output files to be licensed under the GNU General Public
   License without this special exception.

   This special exception was added by the Free Software Foundation in
   version 2.2 of Bison.  */

/* DO NOT RELY ON FEATURES THAT ARE NOT DOCUMENTED in the manual,
   especially those whose name start with YY_ or yy_.  They are
   private implementation details that can be changed or removed.  */

#ifndef YY_YY_Y_TAB_H_INCLUDED
# define YY_YY_Y_TAB_H_INCLUDED
/* Debug traces.  */
#ifndef YYDEBUG
# define YYDEBUG 0
#endif
#if YYDEBUG
extern int yydebug;
#endif

/* Token kinds.  */
#ifndef YYTOKENTYPE
# define YYTOKENTYPE
  enum yytokentype
  {
    YYEMPTY = -2,
    YYEOF = 0,                     /* "end of file"  */
    YYerror = 256,                 /* error  */
    YYUNDEF = 257,                 /* "invalid token"  */
    LEFT_PARENTHESIS = 258,        /* LEFT_PARENTHESIS  */
    RIGHT_PARENTHESIS = 259,       /* RIGHT_PARENTHESIS  */
    LEFT_BRACE = 260,              /* LEFT_BRACE  */
    RIGHT_BRACE = 261,             /* RIGHT_BRACE  */
    NUMBER = 262,                  /* NUMBER  */
    STRING = 263,                  /* STRING  */
    COLON = 264,                   /* COLON  */
    CONST = 265,                   /* CONST  */
    STDOUT = 266,                  /* STDOUT  */
    IDENTIFIER = 267,              /* IDENTIFIER  */
    FUNCTION = 268,                /* FUNCTION  */
    FUNCTION_IDENTIFIER = 269,     /* FUNCTION_IDENTIFIER  */
    PARAM = 270,                   /* PARAM  */
    IF = 271,                      /* IF  */
    ELSE = 272,                    /* ELSE  */
    WHILE = 273,                   /* WHILE  */
    MULTIPLY = 274,                /* MULTIPLY  */
    DIVIDE = 275,                  /* DIVIDE  */
    PLUS = 276,                    /* PLUS  */
    MINUS = 277,                   /* MINUS  */
    ASSIGN = 278,                  /* ASSIGN  */
    SEMICOLON = 279,               /* SEMICOLON  */
    COMMA = 280,                   /* COMMA  */
    AND = 281,                     /* AND  */
    OR = 282,                      /* OR  */
    GT = 283,                      /* GT  */
    LT = 284,                      /* LT  */
    GTE = 285,                     /* GTE  */
    LTE = 286,                     /* LTE  */
    EQ = 287                       /* EQ  */
  };
  typedef enum yytokentype yytoken_kind_t;
#endif
/* Token kinds.  */
#define YYEMPTY -2
#define YYEOF 0
#define YYerror 256
#define YYUNDEF 257
#define LEFT_PARENTHESIS 258
#define RIGHT_PARENTHESIS 259
#define LEFT_BRACE 260
#define RIGHT_BRACE 261
#define NUMBER 262
#define STRING 263
#define COLON 264
#define CONST 265
#define STDOUT 266
#define IDENTIFIER 267
#define FUNCTION 268
#define FUNCTION_IDENTIFIER 269
#define PARAM 270
#define IF 271
#define ELSE 272
#define WHILE 273
#define MULTIPLY 274
#define DIVIDE 275
#define PLUS 276
#define MINUS 277
#define ASSIGN 278
#define SEMICOLON 279
#define COMMA 280
#define AND 281
#define OR 282
#define GT 283
#define LT 284
#define GTE 285
#define LTE 286
#define EQ 287

/* Value type.  */
#if ! defined YYSTYPE && ! defined YYSTYPE_IS_DECLARED
typedef int YYSTYPE;
# define YYSTYPE_IS_TRIVIAL 1
# define YYSTYPE_IS_DECLARED 1
#endif


extern YYSTYPE yylval;


int yyparse (void);


#endif /* !YY_YY_Y_TAB_H_INCLUDED  */
