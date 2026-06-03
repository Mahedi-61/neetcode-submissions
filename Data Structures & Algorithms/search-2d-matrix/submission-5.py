class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROW, COL = len(matrix), len(matrix[0])
        l, r = 0, ROW-1
        while l <= r:
            mid = (l + r) // 2

            if matrix[mid][COL-1] < target:
                l = mid + 1

            elif matrix[mid][0] > target:
                r = mid - 1

            elif matrix[mid][0] <= target and matrix[mid][COL-1] >= target:
                break

        l, r = 0, COL-1
        while l <= r:
            row_mid = (l + r) // 2
            print(l, r, row_mid)

            if matrix[mid][row_mid] < target:
                l = row_mid + 1

            elif matrix[mid][row_mid] > target:
                r = row_mid - 1
            else:
                return True

        return False
