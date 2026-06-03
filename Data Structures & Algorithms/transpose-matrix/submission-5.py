class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        # transposing any matrix (square, rectangle)

        ROW = len(matrix)
        COL = len(matrix[0])
        res = [[0] * ROW for _ in range(COL)]

        for r in range(ROW):
            for c in range(COL):
                res[c][r] = matrix[r][c]

        return res
