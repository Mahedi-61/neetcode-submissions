class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])

        dp = [[0 for _ in range(n)] for _ in range(m)]
        
        # setting first row
        val = 1
        for c in range(n):
            if obstacleGrid[0][c] == 1: val = 0
            dp[0][c] = val
        
        # setting first column
        val = 1
        for r in range(m):
            if obstacleGrid[r][0] == 1: val = 0
            dp[r][0] = val
        
        for r in range(1, m):
            for c in range(1, n):
                if obstacleGrid[r][c] == 1:
                    dp[r][c] = 0
                else:
                    dp[r][c] = dp[r][c-1] + dp[r-1][c]
                    
        return dp[m-1][n-1]