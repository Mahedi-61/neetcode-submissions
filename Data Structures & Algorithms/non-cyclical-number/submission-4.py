class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        def find_squares(n):
            res = 0
            while n:
                res += (n % 10) ** 2
                n = n // 10
            return res
            
        while n:
            if n in seen:
                return False

            elif n == 1:
                return True 

            seen.add(n)
            n = find_squares(n)

        return True