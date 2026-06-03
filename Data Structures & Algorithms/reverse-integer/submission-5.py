class Solution:
    def reverse(self, x: int) -> int:
        max_int = 0x7FFFFFFF
        res = 0
        neg = False
        if x < 0:
            x = abs(x)
            neg = True

        while x:
            res = (res * 10) + x % 10
            x //= 10

            if x != 0 and res > (max_int // 10):
                return 0

        if neg: return -1 * res
        return res
