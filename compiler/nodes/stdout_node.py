from nodes.nodes import Node

class StdoutNode(Node):
  def __init__(self) -> None:
    super().__init__(value=0, children=[])
  
  def evaluate(self, symbol_table) -> None:
    results = [self.children[i].evaluate(symbol_table).value for i in range(len(self.children))]
    print(*results)


