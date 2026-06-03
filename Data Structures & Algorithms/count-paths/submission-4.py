class Solution:
    def uniquePaths(self, m: int, n: int) -> int:


        def dfs(i, j):
            if (i, j) == (0, 0):
                return 1
            elif i < 0 or j < 0:
                return 0
            
            if (i, j) in memo:
                return memo[(i, j)]

            up = dfs(i-1, j)
            left = dfs(i, j-1)
            memo[(i, j)] = up + left
            return memo[(i, j)]
            
        memo = {}
        return dfs(m-1, n-1)
        