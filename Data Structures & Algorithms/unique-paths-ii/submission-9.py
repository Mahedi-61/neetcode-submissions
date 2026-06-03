class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        #top-down approach (dp)
        if obstacleGrid[0][0] == 1:
            return 0
        else:
            obstacleGrid[0][0] = 1

        ROW = len(obstacleGrid)
        COL = len(obstacleGrid[0])

        for r in range(ROW):
            for c in range(COL):
                if (r, c) == (0, 0): continue

                elif obstacleGrid[r][c] == 1:
                    obstacleGrid[r][c] = 0
                
                else:
                    if r == 0:
                        obstacleGrid[r][c] = obstacleGrid[r][c-1]
                    elif c == 0: 
                        obstacleGrid[r][c] += obstacleGrid[r-1][c]
                    else:
                        obstacleGrid[r][c] += obstacleGrid[r-1][c] + obstacleGrid[r][c-1]


        return obstacleGrid[ROW-1][COL-1]