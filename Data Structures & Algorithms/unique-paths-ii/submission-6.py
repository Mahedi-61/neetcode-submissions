class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        
        #bottom-up approach
        ROW = len(obstacleGrid)
        COL = len(obstacleGrid[0])
        if obstacleGrid[0][0] == 1 or obstacleGrid[ROW-1][COL-1] == 1:
            return 0

        for r in range(ROW):
            for c in range(COL):
                if obstacleGrid[r][c] == 1:
                    obstacleGrid[r][c] = "x"

        for c in range(COL-1, -1, -1):
            if obstacleGrid[ROW-1][c] != "x":
                obstacleGrid[ROW-1][c] = 1
            else:
                break
        
        for r in range(ROW-1, -1, -1):
            if obstacleGrid[r][COL-1] != "x":
                obstacleGrid[r][COL-1] = 1
            else:
                break

        for r in range(ROW-2, -1, -1):
            for c in range(COL-2, -1, -1):
                if obstacleGrid[r][c] == "x":
                    obstacleGrid[r][c] = 0

                else:
                    a = obstacleGrid[r+1][c] if obstacleGrid[r+1][c] != "x" else 0
                    b = obstacleGrid[r][c+1] if obstacleGrid[r][c+1] != "x" else 0
                    obstacleGrid[r][c] = a + b

        return obstacleGrid[0][0]