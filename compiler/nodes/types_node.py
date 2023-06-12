from nodes.nodes import Node
from _types._types import TypeValue

class IntVal(Node):
  def __init__(self, value: int) -> None:
    super().__init__(value, children=[])
  
  def evaluate(self, symbol_table) -> TypeValue:
    return TypeValue("integer", self.value)


class StrVal(Node):
  def __init__(self, value: str) -> None:
    super().__init__(value, children=[])
  
  def evaluate(self, symbol_table) -> TypeValue:
    return TypeValue("string", self.value)