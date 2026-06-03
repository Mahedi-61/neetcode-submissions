class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        dp = [*nums]

        for i in range(1, len(nums)):
            dp[i] = max(dp[i - 1] + nums[i], dp[i])

        return max(dp)