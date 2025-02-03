"""
Given the `root` of a binary tree, the value of a target node `target`, and an
integer `k`, return _an array of the values of all nodes that have a
distance_`k` _from the target node._

You can return the answer in **any order**.
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        $$$
