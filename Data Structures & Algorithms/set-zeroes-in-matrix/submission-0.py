class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:

        m, n = len(matrix), len(matrix[0])
        row_z = []
        col_z = []
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    row_z.append(i)
                    col_z.append(j)

        for i in row_z:
            matrix[i] = [0 for _ in range(n)]

        for j in col_z:
            for r in range(m):
                matrix[r][j] = 0
