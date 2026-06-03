class Solution:
    def tribonacci(self, n: int) -> int:
        #space optimized
        dp = [0] * 3
        dp[1] = 1
        dp[2] = 1
        if n < 3:
            return dp[n]

        for i in range(3, n+1):
            temp = dp[2]
            dp[2] = dp[0] + dp[1] + dp[2]
            dp[0] = dp[1]
            dp[1] = temp

        return dp[2] 