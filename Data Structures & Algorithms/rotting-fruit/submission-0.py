class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        #Need multi-source bfs
        ROW = len(grid)
        COL = len(grid[0])

        def bfs(q, visit, count):
            level = 0
            directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
            while q:
                for _ in range(len(q)):
                    i, j = q.popleft()
                    visit.add((i, j))

                    # if not (i - 1 < 0 or grid[i-1][j] == 0 or (i-1, j) in visit):
                    #     q.append((i-1, j))
                    #     count -= 1

                    # if not (i + 1>= ROW or grid[i+1][j] == 0 or (i+1, j) in visit):
                    #     q.append((i+1, j))
                    #     count -= 1

                    # if not (j - 1 < 0 or grid[i][j-1] == 0 or (i, j-1) in visit):
                    #     q.append((i, j-1))
                    #     count -= 1

                    # if not (j + 1>= COL or grid[i][j+1] == 0 or (i, j+1) in visit):
                    #     q.append((i, j+1))
                    #     count -= 1

                    for dr, dc in directions:
                        nr, nc = i + dr, j + dc
                        # Check bounds and whether it's a fresh orange
                        if 0 <= nr < ROW and 0 <= nc < COL and grid[nr][nc] == 1:
                            grid[nr][nc] = 2       # mark as rotten
                            visit.add((nr, nc))
                            q.append((nr, nc))
                            count -= 1    

                if len(q) > 0: 
                    level += 1
 
            return level if count == 0 else -1

        q = collections.deque()
        visit = set()
        count = 0
        for r in range(ROW):
            for c in range(COL):
                if grid[r][c] == 2:
                    q.append((r, c))
                    visit.add((r, c))

                elif grid[r][c] == 1:
                    count += 1

        return bfs(q, visit, count)
