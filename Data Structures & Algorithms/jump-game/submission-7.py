class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        dp = [False] * n
        dp[-1] = True 

        for i in range(n-2, -1, -1):
            start = i + 1
            end = min(i + nums[i], n-1)

            for j in range(start, end + 1):
                if dp[j] == True: 
                    dp[i] = True
                    break

        return dp[0]