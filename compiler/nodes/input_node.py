from nodes import Node
from ..types._types import TypeValue

class InputNode(Node):
  def __init__(self) -> None:
    super().__init__(value="read", children=[])
  
  def evaluate(self, symbol_table) -> TypeValue:
    return TypeValue("Int", int(input(""))) 
