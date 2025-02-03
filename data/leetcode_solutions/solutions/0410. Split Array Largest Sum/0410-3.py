class Solution:
  def splitArray(self, nums: List[int], k: int) -> int:
    l = max(nums)
    r = sum(nums) + 1

    def numGroups(maxSumInGroup: int) -> int:
      groupCount = 1
      sumInGroup = 0

      for num in nums:
        if sumInGroup + num <= maxSumInGroup:
          sumInGroup += num
        else:
          groupCount += 1
          sumInGroup = num

      return groupCount

    while l < r:
      mid = (l + r) // 2
      if numGroups(mid) > k:
        l = mid + 1
      else:
        r = mid

    return l
