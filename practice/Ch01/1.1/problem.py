"""Cracking the Coding Interview 1.1: determine whether a string has all unique characters.

Expose two callables when solving the exercise:

1. ``has_unique_chars(text: str) -> bool``
   - Return ``True`` only if ``text`` contains no repeated characters.
   - Any auxiliary data structures are allowed.

2. ``has_unique_chars_no_extra(text: str) -> bool``
   - Same contract as above, but avoid data structures whose size grows with the input
     (constant-sized helpers are acceptable).

Feel free to replace this module with any structure you prefer; the tests import only the
functions named above.
"""


def has_unique_chars(text: str) -> bool:
    cur_dict: dict[str, bool] = {}
    for ch in text:
        if ch in cur_dict:
            return False
        cur_dict[ch] = True
    return True


def has_unique_chars_no_extra(text: str) -> bool:
    sorted_chars = sorted(text)
    for idx in range(len(sorted_chars) - 1):
        if sorted_chars[idx] == sorted_chars[idx + 1]:
            return False
    return True
