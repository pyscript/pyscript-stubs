# Copyright (c) 2020-2025 Jos Verlinde
# MIT Licensed

from __future__ import annotations

from collections.abc import Callable
from typing import Any

from _typeshed import Incomplete

def js_import(name: str) -> JSModule:
    """Module level __getattr__ that returns an JSModule object for any requested attribute."""
    ...

class JSModule:
    def __init__(self, name: str) -> None: ...
    def __getattr__(self, field: str) -> Any | None: ...

class Worker:
    async def sync(self) -> Callable[[Any], Any]: ...

class XWorker(Worker):
    # https://pyscript.github.io/polyscript/#xworker-options

    polyfill: bool = False
    window: Incomplete = ...

    def __init__(
        self,
        file: str,
        a_sync: bool = ...,
        config: str = ...,
        type: str = ...,  #  pyodide, micropython, ruby-wasm-wasi, wasmoon, webr
        version: str = ...,
        serviceWorker: str = ...,
    ) -> None: ...

    # def isWindowProxy(self, ref:Incomplete) -> bool: ...

class PyWorker(XWorker):
    def __init__(self, name: str) -> None: ...

xworker: XWorker = ...
