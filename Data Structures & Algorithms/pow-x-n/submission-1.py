class Solution:
    def myPow(self, x: float, n: int) -> float:
        if x == 0: return x 
        if n == 0: return 1 

        def recur(x, n, memo={}):
            if n == 0: return 1
            if n == 1: return x

            res = recur(x*x, n//2) if n % 2 == 0 else x * recur(x*x, n//2)
            return res

        if n > 0:
            return recur(x, n)
        elif n < 0:
            return 1 / recur(x, -1 * n)