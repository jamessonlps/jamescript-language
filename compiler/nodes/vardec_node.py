from nodes import Node
from ..types._types import TypeValue

class VariableDeclarationNode(Node):
  """
  @param `value`: type of the variable
  @param `children`: 
    [0] -> name of the variable (`Identifier`)\n
    [1] -> value of the variable
  """
  def __init__(self, value: str, children=[]) -> None:
    super().__init__(value=value, children=children)
  
  def evaluate(self, symbol_table) -> None:
    if len(self.children) > 1:
      item = TypeValue(self.value, self.children[1].evaluate(symbol_table).value)
      symbol_table.create(self.children[0].value, item)
    else:
      if self.value == "Int":
        item = TypeValue(self.value, 0)
      elif self.value == "String":
        item = TypeValue(self.value, "")
      else:
        raise SyntaxError(f"Invalid type of variable declaration: {self.value} :: {self.children[0].value}")
      symbol_table.create(self.children[0].value, item)