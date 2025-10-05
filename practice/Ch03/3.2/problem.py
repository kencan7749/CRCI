"""Cracking the Coding Interview 3.2: design a stack that supports constant-time min.

When you implement the exercise, expose a ``MinStack`` class with the following API:

``MinStack()``
    Construct an empty stack.

``push(value) -> None``
    Push ``value`` onto the stack.

``pop() -> object``
    Remove and return the top element. Raise ``IndexError`` if the stack is empty.

``peek() -> object``
    Return (without removing) the top element. Raise ``IndexError`` if the stack is empty.

``get_min() -> object``
    Return the minimum element currently stored. Raise ``IndexError`` if the stack is empty.

You may add helper methods or attributes as desired; the tests import only ``MinStack``
and expect the public behaviour described above.
"""
