class Solution:
    def jump(self, nums: List[int]) -> int:
        dp = {len(nums)-1: 0}
        target = len(nums) - 1 

        for i in range(len(nums)-2, -1, -1):
            if i + nums[i] >= target:
                min_cnt = []
                for j in range(1, nums[i] + 1):
                    if i + j in dp:
                        min_cnt.append(1 + dp[i + j])

                target = i
                dp[i] = min(min_cnt)

        return dp[0]



