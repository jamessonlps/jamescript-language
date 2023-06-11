from ..prepro.prepro import PrePro
from ..tokens.tokenizer import Tokenizer
from ..tokens.tokens import *
from ..nodes.nodes import Node
from ..nodes import *


def is_factor_token(token: Token) -> bool:
  return isinstance(token, (NumberToken, PlusToken, MinusToken, LeftParenthesisToken, IdentifierToken, DenialToken, ReadlineToken, StringToken))

def is_statement_token(token: Token) -> bool:
  return isinstance(token, (BreakLineToken, IdentifierToken, PrintlnToken, WhileToken, IfToken, ReturnToken, FunctionDeclarationToken))

class Parser():
  tokenizer: Tokenizer = None

  @staticmethod
  def parseRelExpression() -> Node:
    """
    Starting point: get the next token and call parse term.
    """
    
    Parser.tokenizer.selectNext()
    
    if is_factor_token(Parser.tokenizer.next):
      expression = Parser.parseExpression()
      valid_expression = True
      
      while valid_expression:
        if isinstance(Parser.tokenizer.next, CompareEqualToToken):
          Parser.tokenizer.selectNext()
          if is_factor_token(Parser.tokenizer.next):
            expression2 = Parser.parseExpression()
            expression = BinOp(value="==", children=[expression, expression2])
          else:
            raise SyntaxError("After '==', the next token shoud be a valid factor token, but received: ", Parser.tokenizer.next)
        
        elif isinstance(Parser.tokenizer.next, CompareGreaterThenToken):
          Parser.tokenizer.selectNext()
          if is_factor_token(Parser.tokenizer.next):
            expression2 = Parser.parseExpression()
            expression = BinOp(value=">", children=[expression, expression2])
          else:
            raise SyntaxError("After '>', the next token shoud be a valid factor token, but received: ", Parser.tokenizer.next)
        
        elif isinstance(Parser.tokenizer.next, CompareLessThenToken):
          Parser.tokenizer.selectNext()
          if is_factor_token(Parser.tokenizer.next):
            expression2 = Parser.parseExpression()
            expression = BinOp(value="<", children=[expression, expression2])
          else:
            raise SyntaxError("After '<', the next token shoud be a valid factor token, but received: ", Parser.tokenizer.next)
        
        if isinstance(Parser.tokenizer.next, (CompareEqualToToken, CompareLessThenToken, CompareGreaterThenToken)):
          pass
        else:
          valid_expression = False

      return expression
    else:
      raise SyntaxError(f"Error on parseRelExpression. Token received: {Parser.tokenizer.next._value}")


  @staticmethod
  def parseExpression() -> Node:
    
    if is_factor_token(Parser.tokenizer.next):
      term = Parser.parseTerm()
      valid_term = True
      
      while valid_term:
        if isinstance(Parser.tokenizer.next, PlusToken):
          Parser.tokenizer.selectNext()
          if is_factor_token(Parser.tokenizer.next):
            term2 = Parser.parseTerm()
            term = BinOp(value="+", children=[term, term2])
          else:
            raise SyntaxError(f"After '+', the next token shoud be a valid factor token, but received: {Parser.tokenizer.next._value}")
        
        elif isinstance(Parser.tokenizer.next, MinusToken):
          Parser.tokenizer.selectNext()
          if is_factor_token(Parser.tokenizer.next):
            term2 = Parser.parseTerm()
            term = BinOp(value="-", children=[term, term2])
          else:
            raise SyntaxError(f"After '-', the next token shoud be a valid factor token, but received: {Parser.tokenizer.next._value}")
        
        elif isinstance(Parser.tokenizer.next, LogicOrToken):
          Parser.tokenizer.selectNext()
          if is_factor_token(Parser.tokenizer.next):
            term2 = Parser.parseTerm()
            term = BinOp(value="||", children=[term, term2])
          else:
            raise SyntaxError(f"After '||', the next token shoud be a valid factor token, but received: {Parser.tokenizer.next._value}")
        
        elif isinstance(Parser.tokenizer.next, DotToken):
          Parser.tokenizer.selectNext()
          if is_factor_token(Parser.tokenizer.next):
            term2 = Parser.parseTerm()
            term = BinOp(value=".", children=[term, term2])
          else:
            raise SyntaxError(f"After '.', the next token shoud be a valid factor token, but received: {Parser.tokenizer.next._value}")

        if isinstance(Parser.tokenizer.next, (PlusToken, MinusToken, LogicOrToken, DotToken)):
          pass
        else:
          valid_term = False

      return term
    else:
      raise SyntaxError("Error on parseExpression")



  @staticmethod
  def parseTerm() -> Node:

    if is_factor_token(Parser.tokenizer.next):
      factor = Parser.parseFactor()
      Parser.tokenizer.selectNext()
      
      valid_factor = True
      while valid_factor:
        if isinstance(Parser.tokenizer.next, MultiplicationToken):
          Parser.tokenizer.selectNext()
          if is_factor_token(Parser.tokenizer.next):
            factor2 = Parser.parseFactor()
            factor = BinOp(value="*", children=[factor, factor2])
            Parser.tokenizer.selectNext()
          else:
            raise SyntaxError("Multiplication Error")
        
        elif isinstance(Parser.tokenizer.next, DivisionToken):
          Parser.tokenizer.selectNext()
          if is_factor_token(Parser.tokenizer.next):
            factor2 = Parser.parseFactor()
            factor = BinOp(value="/", children=[factor, factor2])
            Parser.tokenizer.selectNext()
          else:
            raise SyntaxError("Division Error")
        
        elif isinstance(Parser.tokenizer.next, LogicAndToken):
          Parser.tokenizer.selectNext()
          if is_factor_token(Parser.tokenizer.next):
            factor2 = Parser.parseFactor()
            factor = BinOp(value="&&", children=[factor, factor2])
            Parser.tokenizer.selectNext()
          else:
            raise SyntaxError("Logical AND operator error")
          
        
        
        if not isinstance(Parser.tokenizer.next, (MultiplicationToken, DivisionToken, LogicAndToken)):
          valid_factor = False
        
      return factor
    else:
      raise SyntaxError("Error on parseTerm")



  @staticmethod
  def parseFactor() -> Node:
    if isinstance(Parser.tokenizer.next, NumberToken):
      return IntVal(value=Parser.tokenizer.next.value)
    
    elif isinstance(Parser.tokenizer.next, StringToken):
      return StrVal(value=Parser.tokenizer.next.value)
    
    elif isinstance(Parser.tokenizer.next, PlusToken):
      Parser.tokenizer.selectNext()
      factor = Parser.parseFactor()
      return UnOp(value="+", children=[factor])
    
    elif isinstance(Parser.tokenizer.next, MinusToken):
      Parser.tokenizer.selectNext()
      factor = Parser.parseFactor()
      return UnOp(value="-", children=[factor])
    
    elif isinstance(Parser.tokenizer.next, LeftParenthesisToken):
      rel_expression = Parser.parseRelExpression()
      if isinstance(Parser.tokenizer.next, RightParenthesisToken):
        return rel_expression
      raise SyntaxError("An opened parenthesis must be closed.")

    elif isinstance(Parser.tokenizer.next, IdentifierToken):
      identifier_value = Parser.tokenizer.next._value
      next_token, _ = Parser.tokenizer.see_next_token()
      if isinstance(next_token, LeftParenthesisToken):
        Parser.tokenizer.selectNext() # here is the left parenthesis
        args = []
        next_token, _ = Parser.tokenizer.see_next_token()
        
        if isinstance(next_token, RightParenthesisToken):
          Parser.tokenizer.selectNext()
        
        while not isinstance(Parser.tokenizer.next, RightParenthesisToken):
          args.append(Parser.parseRelExpression())
          if isinstance(Parser.tokenizer.next, CommaToken):
            pass
          else:
            if not isinstance(Parser.tokenizer.next, RightParenthesisToken):
              raise SyntaxError(f"You must close the function call with ')'. Received: {Parser.tokenizer.next._value}")
        return FunctionCallNode(value=identifier_value, children=args)
      return IdentifierNode(Parser.tokenizer.next._value)

    elif isinstance(Parser.tokenizer.next, DenialToken):
      Parser.tokenizer.selectNext()
      factor = Parser.parseFactor()
      return UnOp(value="!", children=[factor])
    
    elif isinstance(Parser.tokenizer.next, ReadlineToken):
      read_line = InputNode()
      Parser.tokenizer.selectNext()
      if isinstance(Parser.tokenizer.next, LeftParenthesisToken):
        Parser.tokenizer.selectNext()
        if isinstance(Parser.tokenizer.next, RightParenthesisToken):
          return read_line
        else:
          raise SyntaxError("You must close an opened parenthesis on a readline function.")
      else:
        raise SyntaxError("After declare a readline function, you must use an open parenthesis.")
    
    else:
      raise SyntaxError("Error on parseFactor!")


  @staticmethod
  def parseStatement() -> Node:
    statement = None
    
    if is_statement_token(Parser.tokenizer.next):
      if isinstance(Parser.tokenizer.next, BreakLineToken):
        return NoOp()
      
      elif isinstance(Parser.tokenizer.next, IdentifierToken):
        identifier_value = Parser.tokenizer.next._value
        identifier_node = IdentifierNode(Parser.tokenizer.next._value)
        
        Parser.tokenizer.selectNext()
        
        if isinstance(Parser.tokenizer.next, EqualsToken):
          statement = AssignmentNode(children=[
            identifier_node,
            Parser.parseRelExpression()
          ])
        
        elif isinstance(Parser.tokenizer.next, VariableDeclarationToken):
          Parser.tokenizer.selectNext()
          
          if not isinstance(Parser.tokenizer.next, (IntegerTypeToken, StringTypeToken)):
            raise SyntaxError(f"After declare a variable, you must use a type. Token found: {Parser.tokenizer.next._value}")
          
          type_value = Parser.tokenizer.next.value

          # statement = VariableDeclarationNode(Parser.tokenizer.next._value)
          # statement.children.append(identifier_node)
          Parser.tokenizer.selectNext()
          
          if isinstance(Parser.tokenizer.next, EqualsToken):
            rel_expression_node = Parser.parseRelExpression()
            # statement.children.append(rel_expression_node)
            statement = VariableDeclarationNode(
              value=type_value, 
              children=[identifier_node, rel_expression_node]
            )
          else:
            statement = VariableDeclarationNode(
              value=type_value, 
              children=[identifier_node]
            )
        
        elif isinstance(Parser.tokenizer.next, LeftParenthesisToken):
          # Parser.tokenizer.selectNext()
          args = []
          next_token, _ = Parser.tokenizer.see_next_token()

          if isinstance(next_token, RightParenthesisToken):
            Parser.tokenizer.selectNext()

          while not isinstance(Parser.tokenizer.next, RightParenthesisToken):
            args.append(Parser.parseRelExpression())
            if isinstance(Parser.tokenizer.next, CommaToken):
              pass
            else:
              if not isinstance(Parser.tokenizer.next, RightParenthesisToken):
                raise SyntaxError(f"You must close the function call with ')'. Received: {Parser.tokenizer.next._value}")
          statement = FunctionCallNode(value=identifier_value, children=args)
        
        else:
          raise SyntaxError(f"Invalid token after identifier: {Parser.tokenizer.next._value}")
      
      elif isinstance(Parser.tokenizer.next, FunctionDeclarationToken):
        Parser.tokenizer.selectNext()
        if not isinstance(Parser.tokenizer.next, IdentifierToken):
          raise SyntaxError(f"Invalid keyword after 'function' declaration: {Parser.tokenizer.next._value}")
        function_identifier = IdentifierNode(Parser.tokenizer.next.value)

        Parser.tokenizer.selectNext()
        if not isinstance(Parser.tokenizer.next, LeftParenthesisToken):
          raise SyntaxError(f"Invalid keyword after function name: {Parser.tokenizer.next._value}. You must use a '('")
        
        Parser.tokenizer.selectNext()
        function_args = []
        while not isinstance(Parser.tokenizer.next, RightParenthesisToken):
          if not isinstance(Parser.tokenizer.next, IdentifierToken):
            raise SyntaxError(f"Invalid token inside function declaration: {Parser.tokenizer.next._value}")
          var_identifier = IdentifierNode(Parser.tokenizer.next.value)

          Parser.tokenizer.selectNext()
          if not isinstance(Parser.tokenizer.next, VariableDeclarationToken):
            raise SyntaxError(f"You must define a type for the function parameter. Token received: {Parser.tokenizer.next._value}")
          
          Parser.tokenizer.selectNext()
          if not isinstance(Parser.tokenizer.next, (IntegerTypeToken, StringTypeToken)):
            raise SyntaxError(f"Unrecognized type: {Parser.tokenizer.next._value}")
          var_type = Parser.tokenizer.next.value

          function_args.append(
            VariableDeclarationNode(
              value=var_type, 
              children=[var_identifier]
            )
          )
          Parser.tokenizer.selectNext()
          if isinstance(Parser.tokenizer.next, CommaToken):
            Parser.tokenizer.selectNext()
          else:
            if not isinstance(Parser.tokenizer.next, RightParenthesisToken):
              raise SyntaxError(f"You must close the function declaration with ')'. Received: {Parser.tokenizer.next._value}")

        Parser.tokenizer.selectNext()
        if not isinstance(Parser.tokenizer.next, VariableDeclarationToken):
          raise SyntaxError(f"You must define a type for the function return. Token received: {Parser.tokenizer.next._value}")
        
        Parser.tokenizer.selectNext()
        if not isinstance(Parser.tokenizer.next, (IntegerTypeToken, StringTypeToken)):
          raise SyntaxError(f"Unrecognized type: {Parser.tokenizer.next._value}")
        function_return_type = Parser.tokenizer.next.value

        Parser.tokenizer.selectNext()
        if not isinstance(Parser.tokenizer.next, BreakLineToken):
          raise SyntaxError(f"You must use a break line after function declaration. Token received: {Parser.tokenizer.next._value}")

        function_body = BlockNode()
        Parser.tokenizer.selectNext()
        while is_statement_token(Parser.tokenizer.next):
          function_body.children.append(Parser.parseStatement())
          Parser.tokenizer.selectNext()
        
        if not isinstance(Parser.tokenizer.next, EndIfToken):
          raise SyntaxError(f"You must finish a function declaration with 'end'. Received: {Parser.tokenizer.next._value}")
        
        Parser.tokenizer.selectNext()
        statement = FunctionDeclarationNode(
          value=function_return_type, 
          children=[function_identifier, *function_args, function_body]
        )

      elif isinstance(Parser.tokenizer.next, ReturnToken):
        rel_expression_node = Parser.parseRelExpression()
        statement = ReturnNode(children=[rel_expression_node])

      elif isinstance(Parser.tokenizer.next, PrintlnToken):
        statement = StdoutNode()

        Parser.tokenizer.selectNext()

        if isinstance(Parser.tokenizer.next, LeftParenthesisToken):
          rel_expression_node = Parser.parseRelExpression()
          if isinstance(Parser.tokenizer.next, RightParenthesisToken):
            statement.children.append(rel_expression_node)
            Parser.tokenizer.selectNext()
          else:
            raise SyntaxError("You must close an opened parenthesis on the println invocation.")
        else:
          raise SyntaxError("An opening parenthesis is missing on println call.")
        
      elif isinstance(Parser.tokenizer.next, WhileToken):
        statement = WhileNode()
        
        rel_expression_node = Parser.parseRelExpression()
        statement.children.append(rel_expression_node)

        if isinstance(Parser.tokenizer.next, BreakLineToken):
          Parser.tokenizer.selectNext()
          block = BlockNode()

          while is_statement_token(Parser.tokenizer.next):
            statement_loop = Parser.parseStatement()
            block.children.append(statement_loop)
            Parser.tokenizer.selectNext()
          
          if isinstance(Parser.tokenizer.next, EndIfToken):
            Parser.tokenizer.selectNext()
            statement.children.append(block)
          else:
            raise SyntaxError(f"You must finish a while looping with 'end'. Received: {Parser.tokenizer.next._value}")
        else:
          raise SyntaxError(f"After while conditional you must use a break line token. Received: {Parser.tokenizer.next._value}", )


      elif isinstance(Parser.tokenizer.next, IfToken):
        statement = ConditionalNode("if")

        rel_expression_node = Parser.parseRelExpression()
        statement.children.append(rel_expression_node)

        if isinstance(Parser.tokenizer.next, BreakLineToken):
          Parser.tokenizer.selectNext()
          block = BlockNode()

          while is_statement_token(Parser.tokenizer.next):
            statement_loop = Parser.parseStatement()
            block.children.append(statement_loop)
            Parser.tokenizer.selectNext()

          statement.children.append(block)
          
          # Após statement, pode vir ou não um 'else', seguindo do 'end'.
          if isinstance(Parser.tokenizer.next, ElseToken):
            else_statement = ConditionalNode("else")

            Parser.tokenizer.selectNext()

            if isinstance(Parser.tokenizer.next, BreakLineToken):
              Parser.tokenizer.selectNext()

              while is_statement_token(Parser.tokenizer.next):
                else_statement_loop = Parser.parseStatement()
                else_statement.children.append(else_statement_loop)
                Parser.tokenizer.selectNext()

              statement.children.append(else_statement)
            else:
              raise SyntaxError(f"After 'else' conditional you must use a break line token. Received: {Parser.tokenizer.next._value}")
          
          # Após ou não o 'else', vem o 'end'
          if isinstance(Parser.tokenizer.next, EndIfToken):
            Parser.tokenizer.selectNext()
          else:
            raise SyntaxError(f"You must finish a 'if' looping with 'end'. Received: {Parser.tokenizer.next._value}")
        else:
          raise SyntaxError(f"You must finish an 'if' conditional with '\\n'. Token found: {Parser.tokenizer.next._value}")
      
      if isinstance(Parser.tokenizer.next, BreakLineToken):
        return statement
      raise SyntaxError(f"A statement must to finish with '\\n'. Token found: {Parser.tokenizer.next._value}")

    else:
      raise SyntaxError(f"Invalid token in parseStatement: {Parser.tokenizer.next._value}")


  @staticmethod
  def parseBlock() -> Node:
    node_master = BlockNode(value="root")
    
    Parser.tokenizer.selectNext()
    token = Parser.tokenizer.next

    if is_statement_token(token):
      while not (isinstance(token, EndOfFileToken)):
        statement = Parser.parseStatement()
        node_master.children.append(statement)
        Parser.tokenizer.selectNext()
        token = Parser.tokenizer.next
    else:
      raise SyntaxError(f"Invalid first token: {token._value}")
    
    return node_master



  @staticmethod
  def run(code) -> Node:
    remove_comments = PrePro.filter(text=code)
    code_processed = PrePro.add_eof(text=remove_comments)
    
    Parser.tokenizer = Tokenizer(source=code_processed)

    result = Parser.parseBlock()

    if isinstance(Parser.tokenizer.next, EndOfFileToken):
      return result
    raise SyntaxError("Where is EOF?")