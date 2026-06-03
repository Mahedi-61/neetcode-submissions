class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        #Need multi-source bfs
        ROW = len(grid)
        COL = len(grid[0])

        # count the total number of rotten fruits
        d = deque([])
        fresh = 0
        for r in range(ROW):
            for c in range(COL):
                if grid[r][c] == 2:
                    d.append((r, c))
                if grid[r][c] == 1:
                    fresh += 1
        
        step = 0
        #if len(d) == 0: return -1 
        #if fresh == 0: return step

        while d:
            for _ in range(len(d)):
                (r, c) = d.popleft()
                if grid[r][c] == 1:
                    grid[r][c] = 2
                    fresh -= 1

                for dr, dc in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
                    n_r, n_c = r + dr, c + dc
                    
                    if (n_r < 0 or n_r >= ROW or n_c < 0 or n_c >= COL or 
                        grid[n_r][n_c] != 1):
                        continue
                    else:
                        d.append((n_r, n_c))

            if d: step += 1
        return -1 if fresh != 0 else step
