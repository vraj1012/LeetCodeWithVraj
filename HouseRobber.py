# 198. House Robber
class Solution:
    def rob(self, nums: List[int]) -> int:
        # If there are no houses to rob
        if len(nums) == 0:
            return 0
        # If there is only 1 house to rob
        if len(nums) == 1:
            return nums[0]

        # If there are multiple houses to rob
        dp= [0] * len(nums)
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])
        for i in range(2,len(nums)):
            dp[i] = max(nums[i] + dp[i-2], dp[i-1])
        return dp[-1]