"""
Given a **0-indexed** integer array `nums` of size `n` containing all numbers from `1` to `n`, return *the number of increasing quadruplets*.

A quadruplet `(i, j, k, l)` is increasing if:

* `0 <= i < j < k < l < n`, and
* `nums[i] < nums[k] < nums[j] < nums[l]`.
"""
class Solution:
    def countQuadruplets(self, nums: List[int]) -> int:
        $$$