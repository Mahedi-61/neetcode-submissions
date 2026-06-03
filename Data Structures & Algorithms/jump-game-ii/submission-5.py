class Solution:
    def jump(self, nums: List[int]) -> int:
        dp = [0] * len(nums)
        dp[-1] = 1
        for i in range(len(nums)-2, -1, -1):
            if nums[i] == 0:
                continue

            dp[i] = min(dp[i + j] for j in range(1, nums[i]+1) if i+j < len(nums) and dp[i+j] != 0 ) + 1

        return dp[0] - 1