class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        islands_count = 0 
        visit = set()

        def dfs(i, j, node_cnt=0):
            if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]) or grid[i][j] == "0":
                return 0

            if (i, j) in visit:
                return 0

            else:
                visit.add((i, j))
                node_cnt += 1

            dfs(i, j+1, node_cnt) + dfs(i, j-1, node_cnt) + dfs(i+1, j, node_cnt) + dfs(i-1, j, node_cnt)
            return node_cnt

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    temp = dfs(i, j)
                    print(temp)
                    islands_count += 1 if temp > 0 else 0

        return islands_count
