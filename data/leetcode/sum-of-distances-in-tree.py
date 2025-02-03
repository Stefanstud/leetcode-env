"""
There is an undirected connected tree with `n` nodes labeled from `0` to `n -
1` and `n - 1` edges.

You are given the integer `n` and the array `edges` where `edges[i] = [ai,
bi]` indicates that there is an edge between nodes `ai` and `bi` in the tree.

Return an array `answer` of length `n` where `answer[i]` is the sum of the
distances between the `ith` node in the tree and all other nodes.
"""
class Solution:
    def sumOfDistancesInTree(self, n: int, edges: List[List[int]]) -> List[int]:
        $$$
