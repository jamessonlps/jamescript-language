from nodes.nodes import Node
from typing import List
from _types._types import TypeValue

class ReturnNode(Node):
  """
  @param `children`:
    [0] -> value to return (rel_expression)
  """
  def __init__(self, children: List[Node]) -> None:
    super().__init__(value="return", children=children)
  
  def evaluate(self, symbol_table) -> TypeValue:
    return self.children[0].evaluate(symbol_table)