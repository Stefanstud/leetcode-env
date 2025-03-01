"""
You are given two integers `m` and `n` representing the dimensions of a **0-indexed** `m x n` grid.

You are also given a **0-indexed** 2D integer matrix `coordinates`, where `coordinates[i] = [x, y]` indicates that the cell with coordinates `[x, y]` is colored **black**. All cells in the grid that do not appear in `coordinates` are **white**.

A block is defined as a `2 x 2` submatrix of the grid. More formally, a block with cell `[x, y]` as its top-left corner where `0 <= x < m - 1` and `0 <= y < n - 1` contains the coordinates `[x, y]`, `[x + 1, y]`, `[x, y + 1]`, and `[x + 1, y + 1]`.

Return *a **0-indexed** integer array* `arr` *of size* `5` *such that* `arr[i]` *is the number of blocks that contains exactly* `i` ***black** cells*.
"""
class Solution:
    def countBlackBlocks(self, m: int, n: int, coordinates: List[List[int]]) -> List[int]:
        $$$