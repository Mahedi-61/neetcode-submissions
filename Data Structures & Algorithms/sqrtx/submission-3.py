class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0: return 0

        l = 0
        r = x

        while l <= r:
            mid = (l + r) // 2
            if x > mid**2:
                l = mid + 1

            elif x < mid**2:
                r = mid - 1

            else:
                return mid 

        if mid**2 > x:
            return mid - 1

        elif mid**2 < x:
            return mid 