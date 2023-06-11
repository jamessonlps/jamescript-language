from nodes import Node
from typing import List
from nodes import function_table


class FunctionDeclarationNode(Node):
  """
  It's responsible for creating a function in the function table.

  @param `value`: return type of the function
  @param `children`:
    [0]   -> name of the function (`Identifier`)\n
    [...] -> parameters of the function (`VariableDeclarationNode`)\n
    [-1]  -> body of the function (`Block`)
  """
  def __init__(self, value: str, children: List[Node]) -> None:
    super().__init__(value=value, children=children)
    self.num_params = len(children) - 2
    self.return_type = value
  
  def evaluate(self, symbol_table) -> None:
    function_name = self.children[0].value
    function_table.create(function_name, self)
