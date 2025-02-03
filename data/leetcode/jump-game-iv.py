"""
Given an array of integers `arr`, you are initially positioned at the first
index of the array.

In one step you can jump from index `i` to index:

  * `i + 1` where: `i + 1 < arr.length`.
  * `i - 1` where: `i - 1 >= 0`.
  * `j` where: `arr[i] == arr[j]` and `i != j`.

Return _the minimum number of steps_ to reach the **last index** of the array.

Notice that you can not jump outside of the array at any time.
"""
class Solution:
    def minJumps(self, arr: List[int]) -> int:
        $$$
