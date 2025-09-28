"""Cracking the Coding Interview 1.2: check whether two strings are permutations of each other.

Implement your solution from scratch, but make sure to expose the following callable:

``are_permutations(first: str, second: str) -> bool``
    Return ``True`` when ``first`` can be rearranged to form ``second`` (case- and
    whitespace-sensitive). Return ``False`` otherwise. You may add any helper
    functions, classes, or constants you like—tests only rely on this function.
"""

def are_permutations(first: str, second: str) -> bool:
    # 長さチェック
    if len(first) != len(second):
        return False
    # 長さが同じだったら，両方ソートして比較するとはやい?
    sort_first = sorted(first)
    sort_second = sorted(second)
    return sort_first == sort_second