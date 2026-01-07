from __future__ import annotations

from js import Node

class ArrayBuffer:
    def to_bytes(self) -> bytes: ...

class JsNull: ...

class JsProxy:
    nodeType: int
    nodeValue: str
    def append(self, *args: Node | str) -> None: ...
    async def arrayBuffer(self) -> ArrayBuffer: ...
