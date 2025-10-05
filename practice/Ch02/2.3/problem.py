"""Cracking the Coding Interview 2.3: delete a node in the middle of a singly linked list.

When solving this exercise, provide at least the following API:

``class Node``
    A singly linked list node with attributes ``value`` and ``next`` (default ``None``). The
    constructor should accept ``value`` and an optional ``next`` reference.

``delete_middle_node(node: Node) -> None``
    - ``node`` represents neither the first nor the last node in the list.
    - Remove the node from the list given only a reference to that node (no head reference).
    - Mutate the list in place; do not return anything.
    - Raise ``ValueError`` when ``node`` is ``None`` or when it has no ``next`` node (making it
      invalid for this operation).

Feel free to add helpers or additional APIs—the tests import only ``Node`` and
``delete_middle_node``.
"""
