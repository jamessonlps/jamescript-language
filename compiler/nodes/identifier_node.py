from nodes import Node
from ..types._types import TypeValue

class IdentifierNode(Node):
  """
  @param `value`: name of the variable or function
  """
  def __init__(self, value: str) -> None:
    super().__init__(value, children=[])
  
  def evaluate(self, symbol_table) -> TypeValue:
    return symbol_table.getter(self.value)
