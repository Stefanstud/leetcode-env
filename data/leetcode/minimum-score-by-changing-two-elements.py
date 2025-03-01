"""
You are given a **0-indexed** integer array `nums`.

* The **low** score of `nums` is the minimum value of `|nums[i] - nums[j]|` over all `0 <= i < j < nums.length`.
* The **high** score of `nums` is the maximum value of `|nums[i] - nums[j]|` over all `0 <= i < j < nums.length`.
* The **score** of `nums` is the sum of the **high** and **low** scores of nums.

To minimize the score of `nums`, we can change the value of **at most two** elements of `nums`.

Return *the **minimum** possible **score** after changing the value of **at most two** elements o*f `nums`.

Note that `|x|` denotes the absolute value of `x`.
"""
class Solution:
    def minimizeSum(self, nums: List[int]) -> int:
        $$$