"""Cracking the Coding Interview 5.1: insert one bit pattern into another.

When you implement your solution, expose the callable below:

``insert_bits(target: int, source: int, i: int, j: int) -> int``
    - Interpret ``target`` (N) and ``source`` (M) as non-negative integers.
    - Replace the bits in ``target`` from index ``i`` through ``j`` (inclusive, 0-based,
      least-significant bit at index 0) with ``source``.
    - Return the resulting integer.
    - Raise ``ValueError`` when ``i`` or ``j`` is negative, when ``i > j``, or when ``source``
      does not fit within ``j - i + 1`` bits.

Feel free to add helper functions or alternate APIs—the tests rely only on ``insert_bits``
behaving as described above.
"""
