"""
You are given an integer `n` representing the number of nodes in a **perfect binary tree** consisting of nodes numbered from `1` to `n`. The root of the tree is node `1` and each node `i` in the tree has two children where the left child is the node `2 * i` and the right child is `2 * i + 1`.

Each node in the tree also has a **cost** represented by a given **0-indexed** integer array `cost` of size `n` where `cost[i]` is the cost of node `i + 1`. You are allowed to **increment** the cost of **any** node by `1` **any** number of times.

Return *the **minimum** number of increments you need to make the cost of paths from the root to each **leaf** node equal*.

**Note**:

* A **perfect binary tree** is a tree where each node, except the leaf nodes, has exactly 2 children.
* The **cost of a path** is the sum of costs of nodes in the path.
"""
class Solution:
    def minIncrements(self, n: int, cost: List[int]) -> int:
        $$$