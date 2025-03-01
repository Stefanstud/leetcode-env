"""
You are given two **0-indexed** strings `word1` and `word2`.

A **move** consists of choosing two indices `i` and `j` such that `0 <= i < word1.length` and `0 <= j < word2.length` and swapping `word1[i]` with `word2[j]`.

Return `true` *if it is possible to get the number of distinct characters in* `word1` *and* `word2` *to be equal with **exactly one** move.* Return `false` *otherwise*.
"""
class Solution:
    def isItPossible(self, word1: str, word2: str) -> bool:
        $$$