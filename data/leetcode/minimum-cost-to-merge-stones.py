"""
There are `n` piles of `stones` arranged in a row. The `ith` pile has
`stones[i]` stones.

A move consists of merging exactly `k` consecutive piles into one pile, and
the cost of this move is equal to the total number of stones in these `k`
piles.

Return _the minimum cost to merge all piles of stones into one pile_. If it is
impossible, return `-1`.
"""
class Solution:
    def mergeStones(self, stones: List[int], k: int) -> int:
        $$$
