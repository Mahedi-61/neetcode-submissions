class Solution:
    def jump(self, nums: List[int]) -> int:
        dp = [0] * len(nums)
        for i in range(len(nums)-2, -1, -1):
            if nums[i] == 0:
                continue

            elif i + nums[i] >= len(nums) - 1:
                dp[i] = 1

            else:
                dp[i] = min(dp[i + j] for j in range(1, nums[i]+1) if dp[i+j] != 0 ) + 1

        return dp[0]