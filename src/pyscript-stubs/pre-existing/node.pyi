from typing import Optional
from .base import EventTarget
from .document_class import Document
from .element import Element

class Node(EventTarget):
    baseURI: str
    childNodes: list['Node']
    firstChild: 'Node'
    isConnected: bool
    lastChild: 'Node'
    nextSibling: 'Node'
    nodeName: str
    nodeType: int
    nodeValue: any
    ownerDocument: 'Document'
    parentNode: Optional['Node']
    parentElement: Optional['Element']
    previousSibling: Optional['Node']
    textContent: str

    def appendChild(self, childNode: 'Node'): ...
    def cloneNode(self) -> 'Node': ...