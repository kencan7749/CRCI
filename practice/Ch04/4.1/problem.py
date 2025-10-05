"""Cracking the Coding Interview 4.1: determine whether a route exists between two nodes.

Implement your solution from scratch, but make sure to expose the following callable:

``route_exists(graph, start, end) -> bool``
    - ``graph`` will be provided as a mapping from node identifiers to iterables of neighbour
      identifiers (directed edges).
    - Return ``True`` when there is a path from ``start`` to ``end`` (inclusive).
    - Return ``False`` when no such route exists.
    - Treat ``start == end`` as reachable (return ``True``) as long as the node appears in the
      graph.
    - Raise ``KeyError`` if either ``start`` or ``end`` is not present in ``graph``.

Feel free to add helper functions, classes, or alternative representations—the tests import
only ``route_exists``.
"""

def route_exists(graph, start, end) -> bool:
    