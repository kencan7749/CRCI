"""Cracking the Coding Interview 4.2: build a minimal-height binary search tree.

When you solve the exercise, expose these components:

``class Node``
    A binary tree node with attributes ``value``, ``left`` and ``right`` (default ``None``).
    The constructor should accept ``value`` and optional ``left``/``right`` children.

``minimal_bst(sorted_values) -> Node | None``
    - ``sorted_values`` will be an iterable of comparable values in non-decreasing order.
    - Return the root node of a binary search tree with minimal possible height.
    - Return ``None`` if the iterable is empty.

Feel free to add helpers or alternative APIs—the tests only rely on ``Node`` and
``minimal_bst`` behaving as described above.
"""
