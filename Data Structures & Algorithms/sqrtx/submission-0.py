class Solution:
    def mySqrt(self, x: int) -> int:
        if x < 2: return x 

        # linear search
        i = 1
        while i*i <= x:
            i += 1

        if i*i == x:
            return i 
        else:
            return i-1
