class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:

        dp = [1] * len(nums)
        for i in range(len(nums)):
            res = [dp[j] + 1 for j in range(0, i) if nums[j] < nums[i]]
            if res:
                dp[i] = max(res)

        return max(dp)