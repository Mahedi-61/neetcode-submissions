class Solution:

    def reverse(self, x: int) -> int:
        res = 0
        MAX = 2**31 - 1
        MIN = -2**31
        sign = -1 if x < 0 else 1
        x = abs(x)
        
        while x:
            d = x % 10
            x = x // 10
            if res > MAX // 10 or (res == MAX//10 and d > MAX % 10):
                return 0
            else:
                res = 10*res + d
                
        return sign * res
