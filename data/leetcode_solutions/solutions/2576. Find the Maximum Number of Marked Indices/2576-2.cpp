class Solution {
 public:
  int maxNumOfMarkedIndices(vector<int>& nums) {
    sort(nums.begin(), nums.end());

    int i = 0;
    for (int j = nums.size() / 2; j < nums.size(); ++j)
      if (2 * nums[i] <= nums[j] && ++i == nums.size() / 2)
        break;

    return i * 2;
  }
};
