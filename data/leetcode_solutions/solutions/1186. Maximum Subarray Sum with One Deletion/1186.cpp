class Solution {
 public:
  // Very similar to 53. Maximum Subarray
  int maximumSum(vector<int>& arr) {
    // dp[0][i] := max sum subarray ending w/ i (no deletion).
    // dp[1][i] := max sum subarray ending w/ i (at most 1 deletion).
    vector<vector<int>> dp(2, vector<int>(arr.size()));

    dp[0][0] = arr[0];
    dp[1][0] = arr[0];
    for (int i = 1; i < arr.size(); ++i) {
      dp[0][i] = max(arr[i], dp[0][i - 1] + arr[i]);
      dp[1][i] =
          max({arr[i], dp[1][i - 1] + arr[i], dp[0][i - 1] /*delete arr[i]*/});
    }

    return *max_element(begin(dp[1]), end(dp[1]));
  }
};
