class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        ROW = len(matrix)
        COL = len(matrix[0])
        saved_row = 1

        for r in range(ROW):
            for c in range(COL):
                if r == 0:
                    if matrix[r][c] == 0:
                        saved_row = 0
                else:
                    if matrix[r][c] == 0:
                        matrix[0][c] = 0
                        matrix[r][0] = 0

        #zeros based on rows
        for i in range(1, len(matrix)):
            if matrix[i][0] == 0:
                    matrix[i][:] =  [0] * COL

        #zeros based on columns
        for j, c_val in enumerate(matrix[0]):
            if c_val == 0:
                for i in range(len(matrix)):
                    matrix[i][j] = 0

        if saved_row == 0:
            matrix[0][:] = [0] * COL

