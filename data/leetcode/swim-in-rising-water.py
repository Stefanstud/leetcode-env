"""
You are given an `n x n` integer matrix `grid` where each value `grid[i][j]`
represents the elevation at that point `(i, j)`.

The rain starts to fall. At time `t`, the depth of the water everywhere is
`t`. You can swim from a square to another 4-directionally adjacent square if
and only if the elevation of both squares individually are at most `t`. You
can swim infinite distances in zero time. Of course, you must stay within the
boundaries of the grid during your swim.

Return _the least time until you can reach the bottom right square_`(n - 1, n
- 1)` _if you start at the top left square_`(0, 0)`.
"""
class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        $$$
