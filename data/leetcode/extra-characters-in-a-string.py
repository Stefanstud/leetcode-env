"""
You are given a **0-indexed** string `s` and a dictionary of words `dictionary`. You have to break `s` into one or more **non-overlapping** substrings such that each substring is present in `dictionary`. There may be some **extra characters** in `s` which are not present in any of the substrings.

Return *the **minimum** number of extra characters left over if you break up* `s` *optimally.*
"""
class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        $$$