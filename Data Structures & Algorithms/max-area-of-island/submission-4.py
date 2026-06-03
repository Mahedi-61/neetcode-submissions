class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROW = len(grid)
        COL = len(grid[0])

        def dfs(i, j):
            if i >= ROW or i < 0 or j < 0 or j >= COL or grid[i][j] == 0:
                return 0

            grid[i][j] = 0

            return 1 + dfs(i, j+1) + dfs(i, j-1) + dfs(i+1, j) + dfs(i-1,j)

        max_area = 0
        for r in range(ROW):
            for c in range(COL):
                if grid[r][c] == 1:
                    max_area = max(max_area, dfs(r, c))

        return max_area