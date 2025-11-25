from typing import Optional
from node import Node
from element import Element, HTMLElement

class Document(Node):
    def getElementsByClassName(self, names: str) -> list[Element]: ...
    def createElement(self, localName: str, options: Optional[any] = None) -> HTMLElement: ...
