class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        # do recurssion -- not dp
        # do memoiazation -- dp
        # write tabular format -- dp
        # write space optimized version -- dp
        m = len(grid)
        n = len(grid[0])
        memo = {}

        def f(i, j):
            if (i, j) == (m-1, n-1):
                return grid[m-1][n-1]

            if i >= m or j >= n:
                return 0

            if (i, j) in memo:
                return memo[(i, j)]

            down = right = float('inf')
            if i + 1 < m:
                down = f(i+1, j) + grid[i][j]

            if j + 1 < n:
                right = f(i, j+1) + grid[i][j]

            memo[(i, j)] = min(down, right)
            return memo[(i, j)]

        return f(0, 0)