from nodes.nodes import Node
from _types._types import TypeValue

class InputNode(Node):
  def __init__(self) -> None:
    super().__init__(value="read", children=[])
  
  def evaluate(self, symbol_table) -> TypeValue:
    return TypeValue("integer", int(input(""))) 
