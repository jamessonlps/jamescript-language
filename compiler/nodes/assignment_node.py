from nodes.nodes import Node
from typing import List

class AssignmentNode(Node):
  """
  @param `children`:
    [0] -> Identifier\n
    [1] -> RelExpression
  """
  def __init__(self, children: List[Node] = []) -> None:
    super().__init__(value=0, children=children)
  
  def evaluate(self, symbol_table) -> None:
    symbol_table.setter(
      key=self.children[0].value, 
      value=self.children[1].evaluate(symbol_table)
    )
