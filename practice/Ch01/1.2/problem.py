"""Cracking the Coding Interview 1.2: check whether two strings are permutations of each other.

Provide the callable below when solving the problem:

``are_permutations(first: str, second: str) -> bool``
    Return ``True`` if ``first`` can be rearranged to form ``second`` (case and whitespace
    sensitive). Return ``False`` otherwise. You may add any helper definitions you like; the
    tests only rely on this function.
"""


def are_permutations(first: str, second: str) -> bool:
    if len(first) != len(second):
        return False
    return sorted(first) == sorted(second)
