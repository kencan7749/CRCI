"""Cracking the Coding Interview 1.1
Determine whether a string has all unique characters.

This module exposes two functions:

1. has_unique_chars(text: str) -> bool
   - Uses a set for fast lookup (O(n) time, O(n) space).

2. has_unique_chars_no_extra(text: str) -> bool
   - Uses a bit vector (ASCII only) to avoid extra structures that
     grow with the input size (O(n) time, O(1) space).
"""

def has_unique_chars(text: str) -> bool:
    """Check uniqueness using a set (extra data structure allowed)."""
    seen = set()
    for ch in text:
        if ch in seen:
            return False
        seen.add(ch)
    return True


def has_unique_chars_no_extra(text: str) -> bool:
    """Check uniqueness without extra data structures.
    
    Assumes ASCII input (0–127).
    Uses an integer as a bit vector for O(1) space.
    """
    if len(text) > 128:  # pigeonhole principle
        return False

    bitmask = 0
    for ch in text:
        o = ord(ch)
        if o >= 128:  # safety: fall back if outside ASCII
            return _check_via_sort(text)
        bit = 1 << o
        if bitmask & bit:
            return False
        bitmask |= bit
    return True


def _check_via_sort(text: str) -> bool:
    """Fallback: O(n log n) method via sorting, works for Unicode too."""
    s = sorted(text)
    for i in range(len(s) - 1):
        if s[i] == s[i + 1]:
            return False
    return True