class Solution:
  def pathSum(self, root: TreeNode, targetSum: int) -> int:
    if not root:
      return 0

    def dfs(root: TreeNode, targetSum: int) -> int:
      if not root:
        return 0
      return (targetSum == root.val) + \
          dfs(root.left, targetSum - root.val) + \
          dfs(root.right, targetSum - root.val)

    return dfs(root, targetSum) + \
        self.pathSum(root.left, targetSum) + \
        self.pathSum(root.right, targetSum)
