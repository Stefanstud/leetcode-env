"""
You are given a **binary string** `s`, and a **2D** integer array `queries` where `queries[i] = [firsti, secondi]`.

For the `ith` query, find the **shortest substring** of `s` whose **decimal value**, `val`, yields `secondi` when **bitwise XORed** with `firsti`. In other words, `val ^ firsti == secondi`.

The answer to the `ith` query is the endpoints (**0-indexed**) of the substring `[lefti, righti]` or `[-1, -1]` if no such substring exists. If there are multiple answers, choose the one with the **minimum** `lefti`.

*Return an array* `ans` *where* `ans[i] = [lefti, righti]` *is the answer to the* `ith` *query.*

A **substring** is a contiguous non-empty sequence of characters within a string.
"""
class Solution:
    def substringXorQueries(self, s: str, queries: List[List[int]]) -> List[List[int]]:
        $$$