class Solution:
    def minEnd(self, n: int, x: int) -> int:
        #Two pointer solution
        i_x = 1
        i_n = 1
        res = x
        count = 1

        while count < 64:
            if (x & i_x) == 0:
                if ((n-1) & i_n):
                    res = res | i_x
                i_n = i_n << 1
                count += 1

            i_x = i_x << 1
        return res
