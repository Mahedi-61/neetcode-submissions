class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0
        i = 0
        while i < 32:
            bit = n & 1
            n = n >> 1
            res += bit * 2**(31-i)
            i += 1

        return res
