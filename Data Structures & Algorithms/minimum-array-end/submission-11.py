class Solution:
    def minEnd(self, n: int, x: int) -> int:
        # n < 8 [0 - 7]
        # n < 4 [0 - 3]
        # n < 2 [0 - 1]

        # putting (n-1) 1's within x's zeros

        res = 0
        temp = n - 1
        for i in range(64):
            if (x & (1 << i)) > 0:
                res |= 1 << i

            else:
                res |= (temp & 1) << i
                temp >>= 1

        return res