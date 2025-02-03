"""
You are given two integer arrays of the same length `nums1` and `nums2`. In
one operation, you are allowed to swap `nums1[i]` with `nums2[i]`.

  * For example, if `nums1 = [1,2,3, _8_ ]`, and `nums2 = [5,6,7, _4_ ]`, you can swap the element at `i = 3` to obtain `nums1 = [1,2,3,4]` and `nums2 = [5,6,7,8]`.

Return _the minimum number of needed operations to make_`nums1` _and_`nums2`
_**strictly increasing**_. The test cases are generated so that the given
input always makes it possible.

An array `arr` is **strictly increasing** if and only if `arr[0] < arr[1] <
arr[2] < ... < arr[arr.length - 1]`.
"""
class Solution:
    def minSwap(self, nums1: List[int], nums2: List[int]) -> int:
        $$$
