from nodes.nodes import Node
from _types._types import TypeValue

class BinOp(Node):
  def __init__(self, value, children) -> None:
    super().__init__(value=value, children=children)

  def evaluate_int(self, left, right) -> TypeValue:
    """
    Evaluate a binary operation between two integers
    """
    if self.value == "+":
      return TypeValue("integer", left + right)
    
    elif self.value == "-":
      return TypeValue("integer", left - right)
    
    elif self.value == "*":
      return TypeValue("integer", left * right)
    
    elif (self.value == "/"):
      return TypeValue("integer", left // right)
  
    elif (self.value == ">"):
      result = 1 if left > right else 0
      return TypeValue("integer", result)
    
    elif (self.value == "<"):
      result = 1 if left < right else 0
      return TypeValue("integer", result)

    elif (self.value == ">="):
      result = 1 if left >= right else 0
      return TypeValue("integer", result)
    
    elif (self.value == "<="):
      result = 1 if left <= right else 0
      return TypeValue("integer", result)
    
    elif (self.value == "&&"):
      return TypeValue("integer", left and right)
    
    elif (self.value == "||"):
      return TypeValue("integer", left or right)
    
    elif (self.value == "=="):
      result = 1 if left == right else 0
      return TypeValue("integer", result)

    elif (self.value == "!="):
      result = 1 if left != right else 0
      return TypeValue("integer", result)
    
    elif (self.value == "."):
      return TypeValue("string", str(left) + str(right))
    
  def evaluate_str(self, left, right) -> TypeValue:
    """
    Evaluate a binary operation between two strings
    """
    if (self.value == "=="):
      result = 1 if left == right else 0
      return TypeValue("integer", result)

    elif (self.value == "!="):
      result = 1 if left != right else 0
      return TypeValue("integer", result)
    
    elif (self.value == ">"):
      result = 1 if left > right else 0
      return TypeValue("integer", result)
    
    elif (self.value == "<"):
      result = 1 if left < right else 0
      return TypeValue("integer", result)
    
    elif (self.value == "."):
      return TypeValue("string", str(left) + str(right))
    
    else:
      raise SyntaxError(f"Invalid operation between strings: {left} {self.value} {right}")

  def evaluate_any(self, left, right) -> TypeValue:
    """
    Evaluate a binary operation between two different types
    """
    if (self.value == "."):
      return TypeValue("string", str(left) + str(right))
    elif (self.value == "=="):
      result = 1 if left == right else 0
      return TypeValue("integer", result)
    raise SyntaxError(f"Invalid operation: {left} {self.value} {right}")

  def evaluate(self, symbol_table) -> TypeValue:
    type_left, left = self.children[0].evaluate(symbol_table).instance
    type_right, right = self.children[1].evaluate(symbol_table).instance

    # Operações entre inteiros
    if ((type_left == type_right) and type_left == "integer"):
      return self.evaluate_int(left, right)
    
    # Operações entre strings
    elif ((type_left == type_right) and type_left == "string"):
      return self.evaluate_str(left, right)
    
    # Operação entre qualquer tipo
    elif (type_left != type_right):
      return self.evaluate_any(left, right)
    
    raise SyntaxError(f"Cannot evaluate a bin operation: {left} {self.value} {right}")
  


class UnOp(Node):
  def __init__(self, value, children) -> None:
    super().__init__(value, children)

  def evaluate(self, symbol_table) -> TypeValue:
    if (self.value == "+"):
      return TypeValue("integer", self.children[0].evaluate(symbol_table).value)
    elif (self.value == "-"):
      return TypeValue("integer", -self.children[0].evaluate(symbol_table).value)
    elif (self.value == "!"):
      return TypeValue("integer", not self.children[0].evaluate(symbol_table).value)
    else:
      raise SyntaxError(f"Invalid unary operation: value = {self.value} :: children = {self.children[0]}")




class NoOp(Node):
  def __init__(self) -> None:
    super().__init__(value=None, children=None)

  def evaluate(self, symbol_table) -> int:
    pass
