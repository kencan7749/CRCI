"""Cracking the Coding Interview 1.3: URLify a string.

When solving the exercise, expose the callable below:

``urlify(text: str, true_length: int) -> str``
    - Treat ``text`` as a string with sufficient trailing space to hold the modifications.
    - Only the first ``true_length`` characters of ``text`` are considered meaningful input.
    - Return a new string where every space inside that prefix is replaced with ``%20``.
    - Characters beyond ``true_length`` are ignored.
    - Raise ``ValueError`` if ``true_length`` is negative or greater than ``len(text)``.

Feel free to add helper functions or alternate APIs—the tests only rely on ``urlify``.
"""
