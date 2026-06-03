class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        res = []
        for j in range(len(matrix[0])):
            row = [matrix[i][j] for i in range(len(matrix))]
            res.append(row)

        return res