class Solution:
    def myPow(self, x: float, n: int) -> float:
        frac = False
        if n < 0:
            frac = True
            n = abs(n)

        res = 1
        for _ in range(n):
            res *= x
        
        if frac:
            res = 1/res

        return res