class Solution:
    def tribonacci(self, n: int) -> int:
        #space optimized
        t_0, t_1, t_2 = 0, 1, 1
        if n == 0: return t_0
        elif n == 1: return t_1
        elif n == 2: return t_2

        for i in range(3, n+1):
            temp = t_2
            t_2 = t_0 + t_1 + t_2
            t_0 = t_1
            t_1 = temp
             
        return t_2