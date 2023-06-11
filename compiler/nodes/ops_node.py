from nodes import Node
from ..types._types import TypeValue

class BinOp(Node):
  def __init__(self, value, children) -> None:
    super().__init__(value=value, children=children)

  def evaluate_int(self, left, right) -> TypeValue:
    """
    Evaluate a binary operation between two integers
    """
    if self.value == "+":
      return TypeValue("Int", left + right)
    
    elif self.value == "-":
      return TypeValue("Int", left - right)
    
    elif self.value == "*":
      return TypeValue("Int", left * right)
    
    elif (self.value == "/"):
      return TypeValue("Int", left // right)
  
    elif (self.value == ">"):
      result = 1 if left > right else 0
      return TypeValue("Int", result)
    
    elif (self.value == "<"):
      result = 1 if left < right else 0
      return TypeValue("Int", result)
    
    elif (self.value == "&&"):
      return TypeValue("Int", left and right)
    
    elif (self.value == "||"):
      return TypeValue("Int", left or right)
    
    elif (self.value == "=="):
      result = 1 if left == right else 0
      return TypeValue("Int", result)
    
    elif (self.value == "."):
      return TypeValue("String", str(left) + str(right))
    
  def evaluate_str(self, left, right) -> TypeValue:
    """
    Evaluate a binary operation between two strings
    """
    if (self.value == "=="):
      result = 1 if left == right else 0
      return TypeValue("Int", result)
    
    elif (self.value == ">"):
      result = 1 if left > right else 0
      return TypeValue("Int", result)
    
    elif (self.value == "<"):
      result = 1 if left < right else 0
      return TypeValue("Int", result)
    
    elif (self.value == "."):
      return TypeValue("String", str(left) + str(right))

  def evaluate_any(self, left, right) -> TypeValue:
    """
    Evaluate a binary operation between two different types
    """
    if (self.value == "."):
      return TypeValue("String", str(left) + str(right))
    elif (self.value == "=="):
      result = 1 if left == right else 0
      return TypeValue("Int", result)
    raise SyntaxError(f"Invalid operation: {left} {self.value} {right}")

  def evaluate(self, symbol_table) -> TypeValue:
    type_left, left = self.children[0].evaluate(symbol_table).instance
    type_right, right = self.children[1].evaluate(symbol_table).instance

    # Operações entre inteiros
    if ((type_left == type_right) and type_left == "Int"):
      return self.evaluate_int(left, right)
    
    # Operações entre strings
    elif ((type_left == type_right) and type_left == "String"):
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
      return TypeValue("Int", self.children[0].evaluate(symbol_table).value)
    elif (self.value == "-"):
      return TypeValue("Int", -self.children[0].evaluate(symbol_table).value)
    elif (self.value == "!"):
      return TypeValue("Int", not self.children[0].evaluate(symbol_table).value)
    else:
      raise SyntaxError(f"Invalid unary operation: value = {self.value} :: children = {self.children[0]}")




class NoOp(Node):
  def __init__(self) -> None:
    super().__init__(value=None, children=None)

  def evaluate(self, symbol_table) -> int:
    pass
