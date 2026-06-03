class Solution:
    def jump(self, nums: List[int]) -> int:
        # optimization problems
        # greedy vs dp
        dp = [0] * len(nums)
        for i in range(len(nums)-2, -1, -1):
            if nums[i] == 0:
                pass

            elif i + nums[i] >= len(nums) - 1:
                dp[i] = 1
    
            else:
                temp = []
                for j in range(i+1, i+nums[i]+1):
                    if dp[j] == 0: continue
                    temp.append(1 + dp[j])
                dp[i] = min(temp) if temp else 0

        print(dp)
        return dp[0]
        