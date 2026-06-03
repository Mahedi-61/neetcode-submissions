class Solution:
    def binary(self, x):
        dg = []
        while x:
            dg.append(x % 10)
            x = x // 10
        return dg

    def reverse(self, x: int) -> int:
        res = 0
        MAX = 2**31 - 1
        MIN = -2**32
        if x > 0:
            digits = self.binary(x)
            for d in digits:
                if not res >= MAX/10:
                    res = 10*res + d
                else:
                    return 0

            return res

        else:
            digits = self.binary(-x)
            for d in digits:
                if not -res <= MIN/10:
                    res = 10*res + d
                else:
                    return 0
            return -res
