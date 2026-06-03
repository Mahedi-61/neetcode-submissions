class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROW, COL = len(grid), len(grid[0])

        def dfs(i, j, k):
            if (i < 0 or i >= ROW or j < 0 or j >= COL or 
                grid[i][j] == -1):
                return

            if grid[i][j] < k:
                return 

            elif grid[i][j] == 2147483647:
                grid[i][j] = k

            else:
                grid[i][j] = min(k, grid[i][j])
                
            dfs(i + 1, j, k+1)
            dfs(i - 1, j, k+1)
            dfs(i, j + 1, k+1)
            dfs(i, j - 1, k+1)
            
        for r in range(ROW):
            for c in range(COL):
                if grid[r][c] == 0:
                    dfs(r, c, 0)