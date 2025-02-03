"""
There is a bag that consists of items, each item has a number `1`, `0`, or `-1` written on it.

You are given four **non-negative** integers `numOnes`, `numZeros`, `numNegOnes`, and `k`.

The bag initially contains:

* `numOnes` items with `1`s written on them.
* `numZeroes` items with `0`s written on them.
* `numNegOnes` items with `-1`s written on them.

We want to pick exactly `k` items among the available items. Return *the **maximum** possible sum of numbers written on the items*.
"""
class Solution:
    def kItemsWithMaximumSum(self, numOnes: int, numZeros: int, numNegOnes: int, k: int) -> int:
        $$$