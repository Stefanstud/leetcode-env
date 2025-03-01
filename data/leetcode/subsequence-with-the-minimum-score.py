"""
You are given two strings `s` and `t`.

You are allowed to remove any number of characters from the string `t`.

The score of the string is `0` if no characters are removed from the string `t`, otherwise:

* Let `left` be the minimum index among all removed characters.
* Let `right` be the maximum index among all removed characters.

Then the score of the string is `right - left + 1`.

Return *the minimum possible score to make* `t`*a subsequence of* `s`*.*

A **subsequence** of a string is a new string that is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (i.e., `"ace"` is a subsequence of `"abcde"` while `"aec"` is not).
"""
class Solution:
    def minimumScore(self, s: str, t: str) -> int:
        $$$