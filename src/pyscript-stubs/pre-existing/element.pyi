from . import CSSStyleDeclaration
from node import Node

class Element(Node):
     classList: list[str]
     onclick: callable


class HTMLElement(Element):
    style: CSSStyleDeclaration

