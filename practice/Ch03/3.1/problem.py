"""Cracking the Coding Interview 3.1: implement three stacks by sharing a single array.

When you tackle this exercise, expose a ``TripleStack`` class with the following behaviour:

``TripleStack(capacity_per_stack: int)``
    Construct an object that can store up to ``capacity_per_stack`` elements in each
    of three stacks backed by one underlying array.

``push(stack_index: int, value) -> None``
    Push ``value`` onto the stack identified by ``stack_index`` (expected values: 0, 1, 2).
    Raise ``IndexError`` when the stack index is invalid or when the target stack is full.

``pop(stack_index: int) -> object``
    Remove and return the top element. Raise ``IndexError`` if the stack index is invalid or
    the stack is empty.

``peek(stack_index: int) -> object``
    Return (without removing) the top element. Raise ``IndexError`` when the stack is invalid or
    empty.

``is_empty(stack_index: int) -> bool``
    Return ``True`` when the given stack has no elements; otherwise ``False``.

You may add any helper methods (e.g., ``is_full`` or debugging utilities). Feel free to
replace this module entirely once you start coding—the tests only rely on ``TripleStack`` and
its public methods described above.
"""
