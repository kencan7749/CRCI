"""Cracking the Coding Interview 1.1: determine whether a string has all unique characters.

Implement whatever helpers you like, but make sure to expose at least two callables:

1. ``has_unique_chars(text: str) -> bool``
   - Return ``True`` when ``text`` contains no repeated characters.
   - Return ``False`` otherwise.
   - You may use any additional data structures.

2. ``has_unique_chars_no_extra(text: str) -> bool``
   - Same contract as above, but do not rely on extra data structures whose size grows with the
     input (e.g., sets, dicts, lists). Constant-size helpers are permitted.

Feel free to structure the module however you prefer—replace this docstring, add classes, etc.
The tests import these two functions to validate your solution.
"""


def has_unique_chars(text:str) -> bool:
   
   cur_dict = {}
   
   for t in text:
      if t not in cur_dict.keys():
         cur_dict[t] = True
      else:
         return False
   return True
   
   
   
def has_unique_chars_no_extra(text:str) -> bool:
   # sort 
   sort_text = sorted(text)
   # 隣の文字が同じならfalse
   for i in range(len(sort_text)-1):
      if sort_text[i] == sort_text[i+1]:
         return False
   return True
   
   