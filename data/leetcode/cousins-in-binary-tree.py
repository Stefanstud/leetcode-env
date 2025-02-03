"""
Given the `root` of a binary tree with unique values and the values of two
different nodes of the tree `x` and `y`, return `true` _if the nodes
corresponding to the values_`x` _and_`y` _in the tree are **cousins** , or
_`false` _otherwise._

Two nodes of a binary tree are **cousins** if they have the same depth with
different parents.

Note that in a binary tree, the root node is at the depth `0`, and children of
each depth `k` node are at the depth `k + 1`.
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        $$$
