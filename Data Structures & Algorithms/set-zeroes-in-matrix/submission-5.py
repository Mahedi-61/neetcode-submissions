class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        ROW = len(matrix)
        COL = len(matrix[0])

        row_ind = [1] * ROW
        col_ind = [1] * COL

        for i in range(ROW):
            for j in range(COL):
                if matrix[i][j] == 0:
                    row_ind[i] = 0
                    col_ind[j] = 0

        for i in range(ROW):
            if row_ind[i] == 0:
                matrix[i] = [0] * COL
                continue

            for j in range(COL):
                if col_ind[j] == 0:
                    matrix[i][j] = 0

        return  
