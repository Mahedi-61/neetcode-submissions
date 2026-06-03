class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        i = 0
        n = len(matrix)
        while i < n //2:
            matrix[i], matrix[n-1-i] = matrix[n-1-i], matrix[i]
            i += 1

        for r in range(n):
            for c in range(r+1, n):
                matrix[c][r], matrix[r][c] = matrix[r][c],  matrix[c][r]