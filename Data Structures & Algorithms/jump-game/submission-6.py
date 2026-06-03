class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        dp = [False] * n
        dp[n - 1] = True 


        for i in range(n-2, -1, -1):
            start = i + 1
            end = min(i + nums[i], n)

            for j in range(start, end + 1):
                dp[i] = dp[i] or dp[j]
                if dp[i] == True: break

        return dp[0]
