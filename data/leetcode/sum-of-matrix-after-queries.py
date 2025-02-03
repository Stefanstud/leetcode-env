"""
You are given an integer `n` and a **0-indexed** **2D array** `queries` where `queries[i] = [typei, indexi, vali]`.

Initially, there is a **0-indexed** `n x n` matrix filled with `0`'s. For each query, you must apply one of the following changes:

* if `typei == 0`, set the values in the row with `indexi` to `vali`, overwriting any previous values.
* if `typei == 1`, set the values in the column with `indexi` to `vali`, overwriting any previous values.

Return *the sum of integers in the matrix after all queries are applied*.
"""
class Solution:
    def matrixSumQueries(self, n: int, queries: List[List[int]]) -> int:
        $$$