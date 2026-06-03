class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        m, n = len(matrix), len(matrix[0])
        self.prefix_sum = [[0] * (n + 1) for _ in range(m)]
        
        for i in range(m):
            for j in range(n):
                self.prefix_sum[i][j+1] += self.prefix_sum[i][j] + matrix[i][j] 

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        total = 0
        for i in range(row1, row2+1):
            total += self.prefix_sum[i][col2 + 1] - self.prefix_sum[i][col1] 
        
        return total