from .nodes import Node

class WhileNode(Node):
  def __init__(self) -> None:
    super().__init__("while", children=[])
  
  def evaluate(self, symbol_table):
    while (self.children[0].evaluate(symbol_table).value == 1):
      self.children[1].evaluate(symbol_table)