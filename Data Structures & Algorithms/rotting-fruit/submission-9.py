class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROW = len(grid)
        COL = len(grid[0])
        dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        def bfs(q, fruit_c):
            step = 0
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
                            fruit_c -= 1

                if q: step += 1
            return step, fruit_c

        q = collections.deque()
        fruit_c = 0
        for r in range(ROW):
            for c in range(COL):
                if grid[r][c] == 2:
                    q.append((r, c))
                    grid[r][c] = 0 #making rotten fruits empty
                
                elif grid[r][c] == 1:
                    fruit_c += 1

        mins, fruit_c = bfs(q, fruit_c)
        return mins if fruit_c == 0 else -1
