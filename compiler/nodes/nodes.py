from abc import ABC, abstractmethod
from typing import Union, List

from ..tables.symbol_table import SymbolTable
from ..tables.function_table import function_table
from ..types._types import TypeValue


class Node(ABC):
  def __init__(self, value: Union[int, str], children) -> None:
    self.value: Union[int, str] = value
    self.children: List[Node] = children

  @abstractmethod
  def evaluate(self, symbol_table: SymbolTable) -> TypeValue:
    ...


