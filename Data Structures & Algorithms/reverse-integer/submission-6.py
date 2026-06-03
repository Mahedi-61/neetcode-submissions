class Solution:
    def reverse(self, x: int) -> int:
        max_int = 0x7FFFFFFF
        res = 0
        sign = 1
        if x < 0:
            x = abs(x)
            sign = -1

        while x:
            digit = x % 10
            x //= 10

            if res > (max_int // 10) or (res == max_int // 10 and digit > 7):
                return 0

            res = (res * 10) + digit

        return sign * res
