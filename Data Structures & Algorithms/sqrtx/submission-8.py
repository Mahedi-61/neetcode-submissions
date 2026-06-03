class Solution:
    def mySqrt(self, x: int) -> int:
        l, r = 0, x // 2

        while l <= r:
            mid = (l + r) // 2
            mid_sq = mid * mid
            if mid_sq == x:
                return mid

            elif (mid-1) * (mid-1) <= x and x < mid_sq:
                return mid-1

            elif mid_sq < x:
                l = mid + 1

            elif mid_sq > x:
                r = mid - 1

        print(l, r, mid)
        return l