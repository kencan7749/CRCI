"""Cracking the Coding Interview 2.1: remove duplicates from an unsorted linked list.

Implement your solution from scratch, but provide at least the following API:

``class Node``
    A singly linked list node with attributes ``value`` (any type) and ``next`` (another ``Node``
    or ``None``). The constructor should accept ``value`` and an optional ``next`` with default
    ``None``.

``remove_duplicates(head: Node | None) -> Node | None``
    Remove duplicate values from the list, using additional data structures if you wish.
    Return the (possibly unchanged) head node.

``remove_duplicates_no_buffer(head: Node | None) -> Node | None``
    Same contract as above, but do not use extra data structures whose size grows with the
    input. Constant-size helpers are fine. Modify the list in place and return the head.

Feel free to replace these notes with your own implementation once you start coding.
"""
