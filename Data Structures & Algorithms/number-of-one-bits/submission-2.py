class Solution:
    def hammingWeight(self, n: int) -> int:
        c = 0
        while n:
            c += 1 if n & 1 else 0
            n >>= 1
        return c