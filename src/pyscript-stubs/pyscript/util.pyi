"""
Pyscript 2025.2.3 type-stub.
see: https://docs.pyscript.net/2025.2.3/api/
"""
# Copyright (c) 2020-2025 Jos Verlinde
# MIT Licensed

from __future__ import annotations

from typing import Any

def as_bytearray(buffer: Any) -> bytearray:
    """
    Given a JavaScript ArrayBuffer, convert it to a Python bytearray in a
    MicroPython friendly manner.
    """
    ...

class NotSupported:
    """
    Small helper that raises exceptions if you try to get/set any attribute on
    it.
    """

    def __init__(self, name: str, error: BaseException) -> None: ...
    def __repr__(self) -> str: ...
    def __getattr__(self, attr: str) -> Any: ...
    def __setattr__(self, attr: str, value: Any) -> None: ...
    def __call__(self, *args: Any) -> None: ...

def is_awaitable(obj: Any) -> bool:
    """
    Returns a boolean indication if the passed in obj is an awaitable
    function. (MicroPython treats awaitables as generator functions, and if
    the object is a closure containing an async function we need to work
    carefully.)
    """
    ...
