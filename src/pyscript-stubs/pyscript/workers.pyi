"""
Pyscript 2025.2.3 type-stub.
see: https://docs.pyscript.net/2025.2.3/api/
"""
# Copyright (c) 2020-2025 Jos Verlinde
# MIT Licensed

from __future__ import annotations

from typing import Any, Coroutine

from pyodide.ffi import JsProxy

def _get(name: str) -> Any:
    """
    Internal function to get a worker by name.

    Args:
        name: The name of the worker to retrieve

    Returns:
        The worker object
    """
    ...

class _CoroutineJsProxy(JsProxy):
    """Mockup class for functions contained in a worker."""
    def __call__(self, *args: object, **kwargs: object) -> Coroutine[None, None, JsProxy]: ...

class _WorkerJsProxy(JsProxy):
    """Mockup class for worker objects."""
    def __getattr__(self, name: str) -> _CoroutineJsProxy: ...

class _WorkersJsProxy(JsProxy):
    """
    Read-only proxy wrapper for workers container.

    Provides read-only access to worker properties through item
    and attribute access.
    """
    def __getitem__(self, name: str) -> Coroutine[None, None, _WorkerJsProxy]: ...
    def __getattr__(self, name: str) -> Coroutine[None, None, _WorkerJsProxy]: ...

workers: _WorkersJsProxy
"""
Read-only proxy to access named workers.

Provides access to workers created with create_named_worker() by their names.
"""

async def create_named_worker(
    src: str = "",
    name: str = "",
    config: dict[str, Any] | None = ...,
    type: str = ...,
) -> JsProxy:
    """
    Create a named web worker for parallel execution.

    Creates a PyScript worker that runs in a separate thread, allowing
    for parallel execution of Python code. Workers can be accessed later
    via the workers proxy.

    Args:
        src: The Python source code or URL to run in the worker.
             If empty, creates a worker with no initial code.
        name: The name to assign to the worker. Used to access it via
              the workers proxy.
        config: Optional configuration dictionary for the worker.
                Can include interpreter settings and other options.
        type: The worker type/interpreter. Default is "micropython".
              Other options include "pyodide" or "python".

    Returns:
        A worker object that can be used to communicate with the worker

    Example:
        worker = await create_named_worker(
            src="print('Hello from worker')",
            name="my_worker",
            type="micropython"
        )
        # Access later via: workers.my_worker
    """
    ...
