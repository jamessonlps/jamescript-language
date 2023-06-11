from nodes import Node, NoOp

class BlockNode(Node):
  def __init__(self, value="block") -> None:
    super().__init__(value=value, children=[])
  
  def evaluate(self, symbol_table) -> None:
    for child in self.children:
      if not isinstance(child, NoOp) and child is not None:
        result = child.evaluate(symbol_table)
    
    if self.value != "root":
      return result
