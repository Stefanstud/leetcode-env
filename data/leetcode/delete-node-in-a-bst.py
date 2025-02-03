"""
Given a root node reference of a BST and a key, delete the node with the given
key in the BST. Return _the **root node reference** (possibly updated) of the
BST_.

Basically, the deletion can be divided into two stages:

  1. Search for a node to remove.
  2. If the node is found, delete the node.
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        $$$
