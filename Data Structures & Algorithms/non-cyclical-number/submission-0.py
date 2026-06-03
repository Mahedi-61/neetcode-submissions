class Solution:
    def get_digits(self, n):
        res = []
        while (n != 0):
            res.append( n % 10)
            n = n // 10
        return res 

    def isHappy(self, n: int) -> bool:
        if n == 1: return True 
        
        memo = set()
        while n not in memo:
            memo.add(n)
            ls_digits = self.get_digits(n)
            n = sum(d**2 for d in ls_digits)
            if n == 1: break

        return True if n==1 else False  