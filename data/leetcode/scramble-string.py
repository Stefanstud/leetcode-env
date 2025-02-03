"""
We can scramble a string s to get a string t using the following algorithm:

  1. If the length of the string is 1, stop.
  2. If the length of the string is > 1, do the following: 
    * Split the string into two non-empty substrings at a random index, i.e., if the string is `s`, divide it to `x` and `y` where `s = x + y`.
    * **Randomly**  decide to swap the two substrings or to keep them in the same order. i.e., after this step, `s` may become `s = x + y` or `s = y + x`.
    * Apply step 1 recursively on each of the two substrings `x` and `y`.

Given two strings `s1` and `s2` of **the same length** , return `true` if `s2`
is a scrambled string of `s1`, otherwise, return `false`.
"""
class Solution:
    def isScramble(self, s1: str, s2: str) -> bool:
        $$$
