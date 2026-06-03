class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROW = len(heights)
        COL = len(heights[0])
        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        def bfs(r, c, visit):
            q = deque([(r, c)])

            while q:
                (i, j) = q.popleft()
                visit.add((i, j))

                for dr in dirs:
                    (n_i, n_j) = (i + dr[0], j + dr[1])
                    if (n_i < 0 or n_i >= ROW or n_j < 0 or n_j >= COL or (n_i, n_j) in visit):
                        continue

                    if heights[n_i][n_j] >= heights[i][j]:
                        q.append((n_i, n_j))
  
        #pacific
        visit_p = set()
        for r in range(ROW):
            bfs(r, 0, visit_p)
        for c in range(COL):
            bfs(0, c, visit_p)

        #atlantic
        visit_a = set()
        for r in range(ROW):
            bfs(r, COL-1, visit_a)

        for c in range(COL):
            bfs(ROW-1, c, visit_a)

        final_set = visit_p.intersection(visit_a)
        return [[i, j] for (i, j) in final_set]