class Solution:
    def get_rev_digits(self, x):
        dg = []
        while x:
            dg.append(x % 10)
            x = x // 10
        return dg

    def reverse(self, x: int) -> int:
        res = 0
        MAX = 2**31 - 1
        MIN = -2**31
        sign = -1 if x < 0 else 1
        x = abs(x)

        digits = self.get_rev_digits(x)
        for d in digits:
            if not res >= MAX//10:
                res = 10*res + d
            else:
                return 0

        return sign * res
