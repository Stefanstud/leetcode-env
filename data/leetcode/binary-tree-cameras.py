"""
You are given the `root` of a binary tree. We install cameras on the tree
nodes where each camera at a node can monitor its parent, itself, and its
immediate children.

Return _the minimum number of cameras needed to monitor all nodes of the
tree_.
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minCameraCover(self, root: Optional[TreeNode]) -> int:
        $$$
