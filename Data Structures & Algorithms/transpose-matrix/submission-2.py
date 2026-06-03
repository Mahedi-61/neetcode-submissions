class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        # res = []
        # for j in range(len(matrix[0])):
        #     row = [matrix[i][j] for i in range(len(matrix))]
        #     res.append(row)

        # return res

        res = [[0 for _ in range(len(matrix)) ] for _ in range(len(matrix[0]))]
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                res[j][i] = matrix[i][j]
        return res