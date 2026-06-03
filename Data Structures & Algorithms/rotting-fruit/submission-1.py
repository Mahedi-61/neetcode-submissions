class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        #Need multi-source bfs
        ROW = len(grid)
        COL = len(grid[0])

        def bfs(q, count):
            level = 0
            while q:
                for _ in range(len(q)):
                    i, j = q.popleft()

                    for dr, dc in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
                        nr, nc = i + dr, j + dc

                        if 0 <= nr < ROW and 0 <= nc < COL and grid[nr][nc] == 1:
                            grid[nr][nc] = 2     
                            q.append((nr, nc))
                            count -= 1    

                if len(q) > 0: 
                    level += 1
 
            return level if count == 0 else -1

        q = collections.deque()
        count = 0
        for r in range(ROW):
            for c in range(COL):
                if grid[r][c] == 2:
                    q.append((r, c))

                elif grid[r][c] == 1:
                    count += 1

        return bfs(q, count)
