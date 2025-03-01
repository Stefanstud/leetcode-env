"""
There exists an undirected and unrooted tree with `n` nodes indexed from `0` to `n - 1`. You are given an integer `n` and a 2D integer array edges of length `n - 1`, where `edges[i] = [ai, bi]` indicates that there is an edge between nodes `ai` and `bi` in the tree. You are also given an array `coins` of size `n` where `coins[i]` can be either `0` or `1`, where `1` indicates the presence of a coin in the vertex `i`.

Initially, you choose to start at any vertex in the tree. Then, you can perform the following operations any number of times: 

* Collect all the coins that are at a distance of at most `2` from the current vertex, or
* Move to any adjacent vertex in the tree.

Find *the minimum number of edges you need to go through to collect all the coins and go back to the initial vertex*.

Note that if you pass an edge several times, you need to count it into the answer several times.
"""
class Solution:
    def collectTheCoins(self, coins: List[int], edges: List[List[int]]) -> int:
        $$$