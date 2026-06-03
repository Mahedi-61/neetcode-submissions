class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        #O(m*n) solution & O(n) space 
        col = []
        m = len(matrix)
        n = len(matrix[0])

        for row in matrix:
            is_zero = False
            for c in range(len(row)):
                if row[c] == 0:
                    col.append(c)
                    is_zero = True
                    
            if is_zero == True:
                row[:] = [0] * n

        if col:
            for row in matrix:
                for c in col:
                    row[c] = 0 