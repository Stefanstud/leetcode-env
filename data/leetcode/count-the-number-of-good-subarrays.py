"""
Given an integer array `nums` and an integer `k`, return *the number of **good** subarrays of* `nums`.

A subarray `arr` is **good** if it there are **at least** `k` pairs of indices `(i, j)` such that `i < j` and `arr[i] == arr[j]`.

A **subarray** is a contiguous **non-empty** sequence of elements within an array.
"""
class Solution:
    def countGood(self, nums: List[int], k: int) -> int:
        $$$