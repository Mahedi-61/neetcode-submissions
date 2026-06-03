class Solution:
    def minEnd(self, n: int, x: int) -> int:
        res = x
        index_x = index_n = 1

        while index_n <= n-1:
            if x & index_x == 0:
                if (n-1) & index_n:
                    res |= index_x
                index_n <<= 1

            index_x <<= 1

        return res