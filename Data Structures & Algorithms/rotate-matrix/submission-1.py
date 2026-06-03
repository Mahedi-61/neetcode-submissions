class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:

        #swap rows (verticle direction)
        t = 0
        b = len(matrix) - 1

        while t < b:
            matrix[t], matrix[b] = matrix[b], matrix[t]
            t += 1
            b -= 1

        # transpose (square matrix)
        for r in range(len(matrix)):
            c = r + 1

            while c < len(matrix[0]):
                matrix[r][c], matrix[c][r] = matrix[c][r],  matrix[r][c]
                c += 1
