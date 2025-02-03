class Solution:
    def findTheArrayConcVal(self, nums: List[int]) -> int:
        n = len(nums)
        ans = 0 if n % 2 == 0 else nums[n // 2]
        for i in range(n // 2):
            ans += int(str(nums[i]) + str(nums[-i-1]))
        return ans