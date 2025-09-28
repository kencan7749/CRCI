"""Cracking the Coding Interview 1.2: check whether two strings are permutations of each other.

Implement your solution from scratch, but make sure to expose the following callable:

``are_permutations(first: str, second: str) -> bool``
    Return ``True`` when ``first`` can be rearranged to form ``second`` (case- and
    whitespace-sensitive). Return ``False`` otherwise. You may add any helper
    functions, classes, or constants you like—tests only rely on this function.
"""

from collections import Counter

def are_permutations(first: str, second: str) -> bool:
    if len(first) != len(second):
        return False
    return Counter(first) == Counter(second)