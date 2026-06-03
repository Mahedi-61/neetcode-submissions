class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 1: return 1
        l = 1
        r = x // 2

        while l <= r:
            mid = (l + r) // 2
            mid_sq = mid**2
            if mid_sq > x:
                r = mid - 1
            elif mid_sq < x:
                l = mid + 1
            else:
                return mid

        return r