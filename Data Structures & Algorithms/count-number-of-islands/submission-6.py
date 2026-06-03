class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROW = len(grid)
        COL = len(grid[0])

        def dfs_iter(i, j):
            stack = [(i, j)]
            while stack:
                (i, j) = stack.pop()
                #base condition
                if (i < 0 or i >= ROW or j < 0 or j >= COL or
                grid[i][j] == "0"):
                    continue

                #mutating grid as its list of list
                grid[i][j] = "0"
                stack.append((i+1, j))
                stack.append((i-1, j))
                stack.append((i, j+1))
                stack.append((i, j-1))

        count = 0
        for r in range(ROW):
            for c in range(COL):
                if grid[r][c] == "1":
                    dfs_iter(r, c)
                    count += 1
        return count