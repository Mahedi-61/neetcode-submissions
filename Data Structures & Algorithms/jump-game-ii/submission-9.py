class Solution:
    def jump(self, nums: List[int]) -> int:
        dp = [0] * len(nums)

        for i in range(len(nums)-2, -1, -1):
            if nums[i] == 0: continue
            min_val = float('inf')

            for j in range(i+1, i + nums[i] + 1):
                if j == len(nums) - 1:
                    min_val = 0
                    break

                if dp[j] == 0: continue
                if dp[j] < min_val:
                    min_val = min(min_val, dp[j])

            dp[i] = 0 if min_val == float('inf') else min_val + 1

        return dp[0]
