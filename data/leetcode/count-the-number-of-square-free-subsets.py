"""
You are given a positive integer **0-indexed** array `nums`.

A subset of the array `nums` is **square-free** if the product of its elements is a **square-free integer**.

A **square-free integer** is an integer that is divisible by no square number other than `1`.

Return *the number of square-free non-empty subsets of the array* **nums**. Since the answer may be too large, return it **modulo** `109 + 7`.

A **non-empty** **subset** of `nums` is an array that can be obtained by deleting some (possibly none but not all) elements from `nums`. Two subsets are different if and only if the chosen indices to delete are different.
"""
class Solution:
    def squareFreeSubsets(self, nums: List[int]) -> int:
        $$$