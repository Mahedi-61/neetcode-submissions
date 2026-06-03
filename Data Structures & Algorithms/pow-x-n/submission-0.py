class Solution:
    def myPow(self, x: float, n: int) -> float:
        if x == 0: return x 
        if n == 0: return 1 

        def recur(x, n, memo={}):
            if n == 0: return 1
            if n == 1: return x
            if n in memo: return memo[n]

            fh = n // 2
            sh = n - fh 

            memo[fh] = recur(x, fh)
            memo[sh] =  recur(x, sh)
            return  memo[fh] * memo[sh]
        
        if n > 0:
            return recur(x, n)
        elif n < 0:
            return recur(1/x, -1 * n)