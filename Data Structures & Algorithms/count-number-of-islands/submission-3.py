class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        count = 0
        visit = set()
        n_rows = len(grid)
        n_cols = len(grid[0])

        def bfs(i, j):
            visit.add((i, j))
            q = collections.deque()
            q.append((i, j))
            grid_dirs = [[1, 0], [-1, 0], [0, 1], [0, -1]]

            while q:
                i, j = q.popleft()
                
                for dr, dc in grid_dirs:
                    new_r = i + dr
                    new_c = j + dc
                    if (0 <= new_r < n_rows and 0 <= new_c < n_cols and 
                        grid[new_r][new_c] == "1" and (new_r, new_c) not in visit):

                        q.append((new_r, new_c))
                        visit.add((new_r, new_c))
        
        for r in range(n_rows):
            for c in range(n_cols):
                if grid[r][c] == "1" and (r, c) not in visit:
                    bfs(r, c)
                    count += 1
        return count