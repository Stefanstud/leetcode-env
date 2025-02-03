"""
There is a one-dimensional garden on the x-axis. The garden starts at the
point `0` and ends at the point `n`. (i.e The length of the garden is `n`).

There are `n + 1` taps located at points `[0, 1, ..., n]` in the garden.

Given an integer `n` and an integer array `ranges` of length `n + 1` where
`ranges[i]` (0-indexed) means the `i-th` tap can water the area `[i -
ranges[i], i + ranges[i]]` if it was open.

Return _the minimum number of taps_ that should be open to water the whole
garden, If the garden cannot be watered return **-1**.
"""
class Solution:
    def minTaps(self, n: int, ranges: List[int]) -> int:
        $$$
