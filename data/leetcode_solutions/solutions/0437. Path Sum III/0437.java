class Solution {
  public int pathSum(TreeNode root, int targetSum) {
    if (root == null)
      return 0;
    return dfs(root, targetSum) + pathSum(root.left, targetSum) + pathSum(root.right, targetSum);
  }

  private int dfs(TreeNode root, int targetSum) {
    if (root == null)
      return 0;
    return (targetSum == root.val ? 1 : 0) +
        dfs(root.left, targetSum - root.val) +
        dfs(root.right, targetSum - root.val);
  }
}
