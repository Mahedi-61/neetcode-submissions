class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        #tabulation
        dp = [[0] * (n) for _ in range(m)]
        for c in range(n):
            dp[m-1][c] = 1

        for r in range(m):
            dp[r][n-1] = 1

        for i in range(m-2, -1, -1):
            for j in range(n-2, -1, -1):
                dp[i][j] = dp[i+1][j] + dp[i][j+1]

        return dp[0][0]