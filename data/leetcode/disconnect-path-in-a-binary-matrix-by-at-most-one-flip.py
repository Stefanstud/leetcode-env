"""
You are given a **0-indexed** `m x n` **binary** matrix `grid`. You can move from a cell `(row, col)` to any of the cells `(row + 1, col)` or `(row, col + 1)` that has the value `1`. The matrix is **disconnected** if there is no path from `(0, 0)` to `(m - 1, n - 1)`.

You can flip the value of **at most one** (possibly none) cell. You **cannot flip** the cells `(0, 0)` and `(m - 1, n - 1)`.

Return `true` *if it is possible to make the matrix disconnect or* `false` *otherwise*.

**Note** that flipping a cell changes its value from `0` to `1` or from `1` to `0`.
"""
class Solution:
    def isPossibleToCutPath(self, grid: List[List[int]]) -> bool:
        $$$