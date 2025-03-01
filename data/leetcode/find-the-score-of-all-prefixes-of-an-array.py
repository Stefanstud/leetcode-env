"""
We define the **conversion array** `conver` of an array `arr` as follows:

* `conver[i] = arr[i] + max(arr[0..i])` where `max(arr[0..i])` is the maximum value of `arr[j]` over `0 <= j <= i`.

We also define the **score** of an array `arr` as the sum of the values of the conversion array of `arr`.

Given a **0-indexed** integer array `nums` of length `n`, return *an array* `ans` *of length* `n` *where* `ans[i]` *is the score of the prefix* `nums[0..i]`.
"""
class Solution:
    def findPrefixScore(self, nums: List[int]) -> List[int]:
        $$$