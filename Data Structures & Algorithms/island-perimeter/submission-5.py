class Solution:

    def islandPerimeter(self, grid: List[List[int]]) -> int:
        # grid[i][j] = 1 represents land and grid[i][j] = 0 represents water.
        # there is exactly one island (i.e., one or more connected land cells).
        # Return the perimeter of the island.
        # Grid cells are connected horizontally/vertically (not diagonally). 

        visit = set()
        def dfs(i, j):
            # stopping conditiions
            if (i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]) or grid[i][j] == 0):
                return 1
            if (i, j) in visit:
                return 0

            visit.add((i,j))
            perim = dfs(i, j+1) + dfs(i, j-1) + dfs(i-1, j) + dfs(i+1, j)
            return perim


        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    return dfs(i, j)