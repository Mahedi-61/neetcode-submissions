class Solution:
    def jump(self, nums: List[int]) -> int:
        dp = [0] * len(nums)

        for i in range(len(nums)-2, -1, -1):
            if nums[i] != 0:
                ls_jump = []

                for j in range(i+1, i + nums[i] + 1):
                    if j == len(nums) - 1: 
                        ls_jump.append(0)
                        break

                    if dp[j] > 0:
                        ls_jump.append(dp[j])

                dp[i] = 1 + min(ls_jump)

        return dp[0]