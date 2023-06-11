from nodes import Node
from nodes import SymbolTable
    

class ConditionalNode(Node):
  def __init__(self, value: str) -> None:
    super().__init__(value, children=[])
  
  def evaluate(self, symbol_table: SymbolTable):
    # Após o else não há nenhuma condicional
    if self.value == "else":
      self.children[0].evaluate(symbol_table)
    # Se for if, resolve se a condição em children[0] for True
    elif (self.children[0].evaluate(symbol_table).value == 1):
      self.children[1].evaluate(symbol_table)
    # Se a anterior é False e há um else, resolve em children[2]
    elif (len(self.children) >= 3):
      self.children[2].evaluate(symbol_table)