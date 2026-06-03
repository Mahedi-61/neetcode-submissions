class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        n_rows = len(grid)
        n_cols = len(grid[0])
        visit = set()

        def dfs(i, j):
            if (i < 0 or i >= n_rows or j < 0 or j >= n_cols or
                grid[i][j] == 0 or (i, j) in visit):
                return -1
            
            visit.add((i, j))
            s = 1 + dfs(i, j+1)
            s += 1 + dfs(i, j-1)
            s += 1 + dfs(i+1, j)
            s += 1 + dfs(i-1, j)

            return s

        max_count = 0
        for r in range(n_rows):
            for c in range(n_cols):
                if grid[r][c] == 1 and (r, c) not in visit:
                    count = 1 + dfs(r, c)
                    max_count = max(max_count, count)

        return max_count 
        