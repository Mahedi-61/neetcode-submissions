class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        res = []

        visit = set()
        def dfs(i, j):
            if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]) or grid[i][j] == 0:
                return -1

            if (i, j) in visit: return -1
            else: 
                visit.add((i, j))

            a = 1 + dfs(i, j+1) 
            a += 1 + dfs(i, j-1)
            a += 1 + dfs(i+1, j)
            a += 1 + dfs(i-1, j)
            return a 
             

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    res.append(1 + dfs(i, j))

        return max(res) if res else 0