"""
You are given an array `nums` consisting of **positive** integers and an integer `k`.

**Partition** the array into two ordered **groups** such that each element is in exactly **one** group. A partition is called great if the **sum** of elements of each group is greater than or equal to `k`.

Return *the number of **distinct** great partitions*. Since the answer may be too large, return it **modulo** `109 + 7`.

Two partitions are considered distinct if some element `nums[i]` is in different groups in the two partitions.
"""
class Solution:
    def countPartitions(self, nums: List[int], k: int) -> int:
        $$$