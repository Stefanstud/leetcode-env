"""
You are given a 0-indexed two-dimensional integer array `nums`.

Return *the largest **prime** number that lies on at least one of the **diagonals** of* `nums`. In case, no prime is present on any of the diagonals, return *0.*

Note that:

* An integer is **prime** if it is greater than `1` and has no positive integer divisors other than `1` and itself.
* An integer `val` is on one of the **diagonals** of `nums` if there exists an integer `i` for which `nums[i][i] = val` or an `i` for which `nums[i][nums.length - i - 1] = val`.

![](https://assets.leetcode.com/uploads/2023/03/06/screenshot-2023-03-06-at-45648-pm.png)

In the above diagram, one diagonal is **[1,5,9]** and another diagonal is **[3,5,7]**.
"""
class Solution:
    def diagonalPrime(self, nums: List[List[int]]) -> int:
        $$$