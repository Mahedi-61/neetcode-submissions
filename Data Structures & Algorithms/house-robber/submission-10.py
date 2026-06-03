class Solution:
    def rob(self, nums: List[int]) -> int:
        #bottom-up| dp
        
        dp = [0] * (len(nums) + 1)
        dp[1] = nums[0]
        if len(nums) < 2: 
            return dp[len(nums)]

        dp[2] = max(nums[0], nums[1])

        for i in range(3, len(nums)+1):
            dp[i] = max(dp[i-1], dp[i-2] + nums[i-1]) #choosing or not choosing

        return dp[len(nums)]