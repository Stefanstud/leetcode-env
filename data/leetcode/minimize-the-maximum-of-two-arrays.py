"""
We have two arrays `arr1` and `arr2` which are initially empty. You need to add positive integers to them such that they satisfy all the following conditions:

* `arr1` contains `uniqueCnt1` **distinct** positive integers, each of which is **not divisible** by `divisor1`.
* `arr2` contains `uniqueCnt2` **distinct** positive integers, each of which is **not divisible** by `divisor2`.
* **No** integer is present in both `arr1` and `arr2`.

Given `divisor1`, `divisor2`, `uniqueCnt1`, and `uniqueCnt2`, return *the **minimum possible maximum** integer that can be present in either array*.
"""
class Solution:
    def minimizeSet(self, divisor1: int, divisor2: int, uniqueCnt1: int, uniqueCnt2: int) -> int:
        $$$