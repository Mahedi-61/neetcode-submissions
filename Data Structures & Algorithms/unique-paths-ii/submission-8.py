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
                if obstacleGrid[r][c] == 1 and (r > 0 or c > 0):
                    obstacleGrid[r][c] = 0
                
                else:
                    if c > 0:
                        obstacleGrid[r][c] += obstacleGrid[r][c-1]
                    if r > 0: 
                        obstacleGrid[r][c] += obstacleGrid[r-1][c]


        return obstacleGrid[ROW-1][COL-1]