class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        ROW = len(matrix)
        COL = len(matrix[0])
        store_col = 1

        for i in range(ROW):
            for j in range(COL):
                if matrix[i][j] == 0:
                    if i == 0:
                        store_col = 0
                    else:
                        matrix[i][0] = 0
                        matrix[0][j] = 0

        # handling rows
        for i in range(1, ROW):
            if matrix[i][0] == 0:
                matrix[i] = [0] * COL

        # handling cols (xcept first col)
        for j in range(COL):
            if matrix[0][j] == 0:
                for i in range(ROW):
                    matrix[i][j] = 0
                

        if store_col == 0:
            matrix[0] = [0] * COL

        return 
