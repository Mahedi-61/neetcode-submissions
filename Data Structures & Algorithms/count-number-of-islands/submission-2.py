class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visit = set()
        r = len(grid)
        c = len(grid[0])

        def dfs(i, j):
            if i < 0 or i >= r or j < 0 or j >= c or (i, j) in visit or grid[i][j] == '0':
                return

            visit.add((i, j))
            dfs(i, j+1)
            dfs(i, j-1)
            dfs(i+1, j)
            dfs(i-1, j)

        count = 0
        for i in range(r):
            for j in range(c):
                if grid[i][j] == '1' and (i, j) not in visit:
                    count += 1
                    dfs(i, j)

        return count