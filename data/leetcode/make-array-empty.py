"""
You are given an integer array `nums` containing **distinct** numbers, and you can perform the following operations **until the array is empty**:

* If the first element has the **smallest** value, remove it
* Otherwise, put the first element at the **end** of the array.

Return *an integer denoting the number of operations it takes to make* `nums` *empty.*
"""
class Solution:
    def countOperationsToEmptyArray(self, nums: List[int]) -> int:
        $$$