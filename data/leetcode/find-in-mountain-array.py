"""
_(This problem is an **interactive problem**.)_

You may recall that an array `arr` is a **mountain array** if and only if:

  * `arr.length >= 3`
  * There exists some `i` with `0 < i < arr.length - 1` such that: 
    * `arr[0] < arr[1] < ... < arr[i - 1] < arr[i]`
    * `arr[i] > arr[i + 1] > ... > arr[arr.length - 1]`

Given a mountain array `mountainArr`, return the **minimum** `index` such that
`mountainArr.get(index) == target`. If such an `index` does not exist, return
`-1`.

**You cannot access the mountain array directly.** You may only access the
array using a `MountainArray` interface:

  * `MountainArray.get(k)` returns the element of the array at index `k` (0-indexed).
  * `MountainArray.length()` returns the length of the array.

Submissions making more than `100` calls to `MountainArray.get` will be judged
_Wrong Answer_. Also, any solutions that attempt to circumvent the judge will
result in disqualification.
"""
# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
#class MountainArray:
#    def get(self, index: int) -> int:
#    def length(self) -> int:

class Solution:
    def findInMountainArray(self, target: int, mountain_arr: 'MountainArray') -> int:
        $$$
