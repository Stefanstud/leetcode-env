"""
Given a **0-indexed** integer array `nums` of size `n` and two integers `lower` and `upper`, return *the number of fair pairs*.

A pair `(i, j)` is **fair** if:

* `0 <= i < j < n`, and
* `lower <= nums[i] + nums[j] <= upper`
"""
class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        $$$