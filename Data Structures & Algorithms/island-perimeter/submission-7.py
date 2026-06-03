class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        # Counting the number of zeros we hit 
        # dfs will do
        ROW = len(grid)
        COL = len(grid[0])

        def dfs(i, j):
            if i >= ROW or i < 0 or j >= COL or j < 0 or grid[i][j] == 0:
                return 1
            
            elif (i, j) in visit:
                return 0

            visit.add((i, j))

            return dfs(i, j+1) + dfs(i, j-1) + dfs(i+1, j) + dfs(i-1, j)

        visit = set()
        for r in range(ROW):
            for c in range(COL):
                if grid[r][c] == 1:
                    return dfs(r, c) 