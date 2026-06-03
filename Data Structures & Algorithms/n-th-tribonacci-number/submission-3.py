class Solution:
    def tribonacci(self, n: int) -> int:
        dp = [0] * 3
        dp[0] = 0
        dp[1] = 1
        dp[2] = 1
        if n < 3:
            return dp[n]

        for _ in range(3, n + 1):
            temp = sum(dp)
            dp[0] = dp[1]
            dp[1] = dp[2]
            dp[2] = temp

        return temp