class Solution:
  def splitArray(self, nums: List[int], k: int) -> int:
    n = len(nums)
    prefix = [0] + list(itertools.accumulate(nums))

    # dp(i, k) := min of largest sum to split first i nums into k groups
    @functools.lru_cache(None)
    def dp(i: int, k: int) -> int:
      if k == 1:
        return prefix[i]

      ans = math.inf

      # Try all possible partitions
      for j in range(k - 1, i):
        ans = min(ans, max(dp(j, k - 1), prefix[i] - prefix[j]))

      return ans

    return dp(n, k)
