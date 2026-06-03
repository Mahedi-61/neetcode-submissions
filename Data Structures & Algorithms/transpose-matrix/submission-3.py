class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        m = len(matrix)
        n = len(matrix[0])

        res = [] 
        for j in range(n):
            res.append([ matrix[i][j] for i in range(m) ])

        return res