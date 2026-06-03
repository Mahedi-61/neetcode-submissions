class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        #single source bfs

        ROW = len(grid)
        COL = len(grid[0])
        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        def bfs(q):
            step = 0
            while q:
                step += 1
                for _ in range(len(q)):
                    (r, c) = q.popleft()

                    for dr, dc in dirs:
                        n_r, n_c = r + dr, c + dc 

                        if (n_r < 0 or n_r >= ROW or n_c < 0 or n_c >= COL or grid[n_r][n_c] == -1 or (n_r, n_c) in visited):
                            continue

                        visited.add((n_r, n_c))
                        q.append((n_r, n_c))

                        if grid[n_r][n_c] > 0:
                            grid[n_r][n_c] = min(grid[n_r][n_c], step)
                
        for r in range(ROW):
            for c in range(COL):
                if grid[r][c] == 0:
                    visited = set()
                    q = deque([(r, c)])
                    bfs(q)