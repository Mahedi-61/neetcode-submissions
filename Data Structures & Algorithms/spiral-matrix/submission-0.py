class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m = len(matrix)
        n = len(matrix[0])

        top = 0 
        down = m - 1
        left = 0 
        right = n - 1
        result = []
        direct = 0

        while top <= down and left <= right:
            direct = direct % 4

            if direct == 0:
                for i in range(left, right+1):
                    result.append(matrix[top][i])
                top += 1

            elif direct == 1:
                for j in range(top, down+1):
                    result.append(matrix[j][right])
                right -= 1

            elif direct == 2:
                for i in range(right, left-1, -1):
                    result.append(matrix[down][i])
                down -= 1

            elif direct == 3:
                for j in range(down, top-1, -1):
                    result.append(matrix[j][left])
                left += 1

            direct += 1
        
        return result