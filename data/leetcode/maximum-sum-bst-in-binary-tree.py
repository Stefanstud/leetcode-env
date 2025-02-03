"""
Given a **binary tree** `root`, return _the maximum sum of all keys of **any**
sub-tree which is also a Binary Search Tree (BST)_.

Assume a BST is defined as follows:

  * The left subtree of a node contains only nodes with keys **less than** the node's key.
  * The right subtree of a node contains only nodes with keys **greater than** the node's key.
  * Both the left and right subtrees must also be binary search trees.
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxSumBST(self, root: Optional[TreeNode]) -> int:
        $$$
