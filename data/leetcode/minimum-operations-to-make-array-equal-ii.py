"""
You are given two integer arrays `nums1` and `nums2` of equal length `n` and an integer `k`. You can perform the following operation on `nums1`:

* Choose two indexes `i` and `j` and increment `nums1[i]` by `k` and decrement `nums1[j]` by `k`. In other words, `nums1[i] = nums1[i] + k` and `nums1[j] = nums1[j] - k`.

`nums1` is said to be **equal** to `nums2` if for all indices `i` such that `0 <= i < n`, `nums1[i] == nums2[i]`.

Return *the **minimum** number of operations required to make* `nums1` *equal to* `nums2`. If it is impossible to make them equal, return `-1`.
"""
class Solution:
    def minOperations(self, nums1: List[int], nums2: List[int], k: int) -> int:
        $$$