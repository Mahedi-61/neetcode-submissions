class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        ROW = len(grid)
        COL = len(grid[0])

        #O(1) space solution
        for j in range(1, COL):
            grid[0][j] += grid[0][j-1]

        for i in range(1, ROW):
            grid[i][0] += grid[i-1][0]

        for i in range(1, ROW):
            for j in range(1, COL):
                grid[i][j] += min(grid[i-1][j], grid[i][j-1])

        return grid[ROW-1][COL-1]
        