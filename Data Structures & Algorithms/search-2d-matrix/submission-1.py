class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])
        t = 0
        b = len(matrix) - 1

        l = 0
        r = n - 1
        mid_col = (l + r) // 2
        
        while t <= b:
            mid_row = (t + b) // 2
            if matrix[mid_row][0] <= target <= matrix[mid_row][n-1]:
                break

            elif target > matrix[mid_row][n-1]:
                t = mid_row + 1

            elif target < matrix[mid_row][0]:
                b = mid_row - 1

        while(l <= r):
            mid_col = (l + r) // 2
            if matrix[mid_row][mid_col] == target:
                return True 

            elif target > matrix[mid_row][mid_col]:
                l = mid_col + 1
            else:
                r = mid_col - 1

        return False

        