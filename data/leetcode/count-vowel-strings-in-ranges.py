"""
You are given a **0-indexed** array of strings `words` and a 2D array of integers `queries`.

Each query `queries[i] = [li, ri]` asks us to find the number of strings present in the range `li` to `ri` (both **inclusive**) of `words` that start and end with a vowel.

Return *an array* `ans` *of size* `queries.length`*, where* `ans[i]` *is the answer to the* `i`th *query*.

**Note** that the vowel letters are `'a'`, `'e'`, `'i'`, `'o'`, and `'u'`.
"""
class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        $$$