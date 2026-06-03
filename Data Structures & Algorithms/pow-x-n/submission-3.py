class Solution:
    def myPow(self, x: float, n: int) -> float:
        def find_power(x, power):
            if x == 0: return 0
            if power == 0: return 1
            if power == 1: return x
            
            if (power & 1) == 1: 
                return x * find_power(x, power//2) ** 2
            else: 
                return find_power(x, power //2) ** 2
        
        if n >= 0:
            res = find_power(x, n)
        else:
            res = 1 / find_power(x, abs(n))
        return res