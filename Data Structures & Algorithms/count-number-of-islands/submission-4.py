class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROW = len(grid)
        COL = len(grid[0])

        def dfs(i, j):
            #base condition
            if (i < 0 or i >= ROW or j < 0 or j >= COL or
               grid[i][j] == "0" or (i, j) in visit):
                return

            visit.add((i, j))
            dfs(i+1, j)
            dfs(i-1, j)
            dfs(i, j+1)
            dfs(i, j-1)

        visit = set()
        count = 0
        for r in range(ROW):
            for c in range(COL):
                if grid[r][c] == "1" and (r, c) not in visit:
                    dfs(r, c)
                    count += 1

        return count