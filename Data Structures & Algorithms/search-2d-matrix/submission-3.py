class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        t = 0
        b = len(matrix) - 1

        while t <= b:
            mid = (t + b) // 2
            if target < matrix[mid][0]:
                b = mid - 1

            elif target > matrix[mid][-1]:
                t = mid + 1
            else:
                break

        l = 0
        r = len(matrix[0]) - 1
        while l <= r:
            cent = (l + r) // 2
            if target < matrix[mid][cent]:
                r = cent - 1

            elif target > matrix[mid][cent]:
                l = cent + 1

            elif target == matrix[mid][cent]:
                return True

        return False