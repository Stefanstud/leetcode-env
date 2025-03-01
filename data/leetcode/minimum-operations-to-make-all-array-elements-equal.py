"""
You are given an array `nums` consisting of positive integers.

You are also given an integer array `queries` of size `m`. For the `ith` query, you want to make all of the elements of `nums` equal to `queries[i]`. You can perform the following operation on the array **any** number of times:

* **Increase** or **decrease** an element of the array by `1`.

Return *an array* `answer` *of size* `m` *where* `answer[i]` *is the **minimum** number of operations to make all elements of* `nums` *equal to* `queries[i]`.

**Note** that after each query the array is reset to its original state.
"""
class Solution:
    def minOperations(self, nums: List[int], queries: List[int]) -> List[int]:
        $$$