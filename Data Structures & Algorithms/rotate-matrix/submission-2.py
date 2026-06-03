class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix) #2
        t = 0
        b = n - 1 #1

        while t < b:
            matrix[t][:], matrix[b][:] = matrix[b][:], matrix[t][:]
            t += 1
            b -= 1

        k = 0
        while k != n - 1: # 0 != 1
            for i in range(k+1, n):
                matrix[k][i], matrix[i][k] = matrix[i][k], matrix[k][i]

            k += 1
        return 

        