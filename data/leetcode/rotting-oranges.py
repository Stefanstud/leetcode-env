"""
You are given an `m x n` `grid` where each cell can have one of three values:

  * `0` representing an empty cell,
  * `1` representing a fresh orange, or
  * `2` representing a rotten orange.

Every minute, any fresh orange that is **4-directionally adjacent** to a
rotten orange becomes rotten.

Return _the minimum number of minutes that must elapse until no cell has a
fresh orange_. If _this is impossible, return_ `-1`.
"""
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        $$$
