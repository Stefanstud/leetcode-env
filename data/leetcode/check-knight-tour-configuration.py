"""
There is a knight on an `n x n` chessboard. In a valid configuration, the knight starts **at the top-left cell** of the board and visits every cell on the board **exactly once**.

You are given an `n x n` integer matrix `grid` consisting of distinct integers from the range `[0, n * n - 1]` where `grid[row][col]` indicates that the cell `(row, col)` is the `grid[row][col]th` cell that the knight visited. The moves are **0-indexed**.

Return `true` *if* `grid` *represents a valid configuration of the knight's movements or* `false` *otherwise*.

**Note** that a valid knight move consists of moving two squares vertically and one square horizontally, or two squares horizontally and one square vertically. The figure below illustrates all the possible eight moves of a knight from some cell.

![](https://assets.leetcode.com/uploads/2018/10/12/knight.png)
"""
class Solution:
    def checkValidGrid(self, grid: List[List[int]]) -> bool:
        $$$