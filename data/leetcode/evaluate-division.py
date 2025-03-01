"""
You are given an array of variable pairs `equations` and an array of real
numbers `values`, where `equations[i] = [Ai, Bi]` and `values[i]` represent
the equation `Ai / Bi = values[i]`. Each `Ai` or `Bi` is a string that
represents a single variable.

You are also given some `queries`, where `queries[j] = [Cj, Dj]` represents
the `jth` query where you must find the answer for `Cj / Dj = ?`.

Return _the answers to all queries_. If a single answer cannot be determined,
return `-1.0`.

**Note:** The input is always valid. You may assume that evaluating the
queries will not result in division by zero and that there is no
contradiction.
"""
class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        $$$
