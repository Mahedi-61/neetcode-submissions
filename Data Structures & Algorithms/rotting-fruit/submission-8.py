class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROW = len(grid)
        COL = len(grid[0])
        dirs = [[0, 1], [0, -1], [1, 0], [-1, 0]]

        def bfs(q):
            count = 0
            while q:
                for _ in range(len(q)):
                    (r, c) = q.popleft()
                    for d in dirs:
                        (n_r, n_c) = (r + d[0], c + d[1])

                        if (n_r >= ROW or n_r < 0 or n_c < 0 or n_c >= COL or grid[n_r][n_c] == 0): 
                            continue

                        if grid[n_r][n_c] == 1:
                            q.append((n_r, n_c))
                            grid[n_r][n_c] = 0

                if q: count += 1
            return count

        q = collections.deque()
        f_cords = []
        for r in range(ROW):
            for c in range(COL):
                if grid[r][c] == 2:
                    q.append((r, c))
                    grid[r][c] = 0 #making rotten fruits empty
                
                elif grid[r][c] == 1:
                    f_cords.append((r,c))

        count = bfs(q)
        for (i, j) in f_cords:
            if grid[i][j] == 1:
                return -1

        return count
