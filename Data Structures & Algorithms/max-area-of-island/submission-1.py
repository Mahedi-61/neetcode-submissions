class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        n_rows = len(grid)
        n_cols = len(grid[0])
        visit = set()

        def dfs(i, j):
            if (i < 0 or i >= n_rows or j < 0 or j >= n_cols or
                grid[i][j] == 0 or (i, j) in visit):
                return 
            
            visit.add((i, j))
            # dirs = [[1, 1], [1, -1], [-1, 1], [-1, -1]]
            # for dr, dc in dirs:
            #     n_r, n_c = i + dr, j + dc
            #     if (0 <= n_r < n_rows and 0 <= n_c < n_cols and grid[n_r][n_c] == 1):
            #         cell =- 2501
            #         visit.add((n_r, n_c))

            dfs(i, j+1)
            dfs(i, j-1)
            dfs(i+1, j)
            dfs(i-1, j)

        max_count = 0
        for r in range(n_rows):
            for c in range(n_cols):
                if grid[r][c] == 1 and (r, c) not in visit:
                    count = len(visit)
                    dfs(r, c)

                    print(len(visit) - count)
                    max_count = max(max_count, len(visit) - count)

        return max_count 
        