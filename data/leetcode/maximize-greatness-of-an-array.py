"""
You are given a 0-indexed integer array `nums`. You are allowed to permute `nums` into a new array `perm` of your choosing.

We define the **greatness** of `nums` be the number of indices `0 <= i < nums.length` for which `perm[i] > nums[i]`.

Return *the **maximum** possible greatness you can achieve after permuting* `nums`.
"""
class Solution:
    def maximizeGreatness(self, nums: List[int]) -> int:
        $$$