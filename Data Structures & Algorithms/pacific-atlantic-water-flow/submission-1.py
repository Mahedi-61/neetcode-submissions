class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:

        ROW = len(heights)
        COL = len(heights[0])

        data = [(ROW - 1, j) for j in range(COL)]
        data +=  [(i, COL - 1) for i in range(ROW)]
        atlantic_set = set(data)

        data = [(0, j) for j in range(COL)]
        data +=  [(i, 0) for i in range(ROW)]
        pacific_set = set(data)

        def dfs(i, j, move="", val=0):
            if (i < 0 or j < 0 or i >= len(heights) or j >= len(heights[0]) or 
                (i, j) in visit): return

            if move == "up" and heights[i][j] < val: return
            elif move == "down" and heights[i][j] < val: return
            elif move == "left" and heights[i][j] < val: return
            elif move == "right" and heights[i][j] < val: return

            visit.add((i, j))
            dfs(i, j - 1, "up", heights[i][j])
            dfs(i, j + 1, "down", heights[i][j])
            dfs(i - 1, j, "left", heights[i][j])
            dfs(i + 1, j, "right", heights[i][j])

        visit = set()
        for (i, j) in atlantic_set:
            dfs(i, j)

        res_a = visit.copy()
        res_a.update(atlantic_set)

        visit = set()
        for (i, j) in pacific_set:
            dfs(i, j)
        res_p = visit.copy()
        res_p.update(pacific_set)

        return list(res_p & res_a)



