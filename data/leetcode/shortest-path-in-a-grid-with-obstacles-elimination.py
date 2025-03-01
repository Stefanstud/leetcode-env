"""
You are given an `m x n` integer matrix `grid` where each cell is either `0`
(empty) or `1` (obstacle). You can move up, down, left, or right from and to
an empty cell in **one step**.

Return _the minimum number of **steps** to walk from the upper left corner
_`(0, 0)` _to the lower right corner_`(m - 1, n - 1)` _given that you can
eliminate **at most** _`k` _obstacles_. If it is not possible to find such
walk return `-1`.
"""
class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        $$$
