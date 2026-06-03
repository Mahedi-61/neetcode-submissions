class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        ROW = len(grid)
        COL = len(grid[0])

        dp = [[ 0 for _ in range(COL)] for _ in range(ROW)]
        dp[0][0] = grid[0][0]
        for j in range(1, COL):
            dp[0][j] = dp[0][j-1] + grid[0][j]

        for i in range(1, ROW):
            dp[i][0] = dp[i-1][0] + grid[i][0]


        for i in range(1, ROW):
            for j in range(1, COL):
                dp[i][j] = grid[i][j] + min(dp[i-1][j], dp[i][j-1])

        return dp[ROW-1][COL-1]
        