from nodes.nodes import Node

class StdoutNode(Node):
  def __init__(self) -> None:
    super().__init__(value=0, children=[])
  
  def evaluate(self, symbol_table) -> None:
    print(self.children[0].evaluate(symbol_table).value)


