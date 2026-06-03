class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROW = len(grid) #5
        COL = len(grid[0]) #5

        def dfs(i, j):
            if i >= ROW or i < 0 or j >= COL or j < 0 or grid[i][j] == 0 or (i, j) in visit:
                return 0

            visit.add((i, j))
            return 1 + dfs(i+1, j) + dfs(i-1,j) + dfs(i,j+1) + dfs(i,j-1)


        visit = set()
        max_area = 0
        for r in range(ROW):
            for c in range(COL):
                if grid[r][c] == 1 and (r, c) not in visit:
                    area = dfs(r, c)
                    max_area = max(max_area, area)

        return max_area
