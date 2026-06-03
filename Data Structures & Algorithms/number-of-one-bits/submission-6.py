class Solution:
    def hammingWeight(self, n: int) -> int:

        res = 0
        while n:
            count = n ^ 1
            n = n >> 1
            if count % 2 == 0:
                res += 1

        return res