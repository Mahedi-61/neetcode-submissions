class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROW = len(grid)
        COL = len(grid[0])

        def bfs(i, j):
            q = collections.deque()
            q.append((i, j))
            dirs = [[0, 1], [0, -1], [1, 0], [-1, 0]]
            area = 0

            while q:
                (i, j) =  q.popleft()
                if i < 0 or i >= ROW or j < 0 or j >= COL or grid[i][j] == 0:
                    continue
                
                grid[i][j] = 0
                area += 1

                for d in dirs:
                    n_i, n_j = i + d[0], j + d[1]
                    q.append((n_i, n_j))

            return area
                
        max_area = 0
        for r in range(ROW):
            for c in range(COL):
                if grid[r][c] == 1:
                    max_area = max(max_area, bfs(r, c))

        return max_area