"""Cracking the Coding Interview 2.2: return the k-th to last element of a singly linked list.

When you solve the exercise, provide at least these components:

``class Node``
    A singly linked list node with attributes ``value`` and ``next`` (default ``None``).
    The constructor should accept ``value`` and an optional ``next`` node.

``kth_to_last(head: Node | None, k: int) -> Node | None``
    - Interpret ``k`` as 1-based (``k == 1`` returns the final node).
    - Raise ``ValueError`` when ``k`` is less than 1.
    - Return ``None`` if the list contains fewer than ``k`` elements.
    - You may modify the list in place if convenient, but the tests only read the node returned
      (and the structure it links to).

Feel free to delete this note once you start coding and organise the module however you like.
"""
