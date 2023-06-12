from nodes.nodes import Node
from typing import List
from tables.symbol_table import SymbolTable
from tables.function_table import function_table
from _types._types import TypeValue

class FunctionCallNode(Node):
  """
  @param `value`: name of the function
  @param `children`: parameters of the function (Identifier, IntVal, StrVal, BinOp, UnOp)
  """
  def __init__(self, value: str, children: List[Node]) -> None:
    super().__init__(value=value, children=children)

  def evaluate(self, symbol_table) -> TypeValue:
    function_dec = function_table.getter(self.value)

    if (function_dec.num_params != len(self.children)):
      raise SyntaxError(f"Number of params expected: {function_dec.num_params}. Received: {len(self.children)}")
    
    function_symbol_table = SymbolTable(name=self.value)
    
    for i in range(len(self.children)):
      type_expected = function_dec.children[i+1].value
      type_received, arg_received = self.children[i].evaluate(symbol_table).instance
      
      if type_expected != type_received:
        raise SyntaxError(f"Type param mismatch on function '{self.value}': {type_expected} != {type_received}")
      
      function_dec.children[i+1].evaluate(function_symbol_table)
      function_symbol_table.setter(function_dec.children[i+1].children[0].value, TypeValue(type_expected, arg_received))
  
    return_value: TypeValue = function_dec.children[-1].evaluate(function_symbol_table)

    if return_value.type != function_dec.return_type:
      raise SyntaxError(f"Type mismatch on function '{self.value}' return type: {function_dec.return_type} != {return_value.type}")
    
    return return_value