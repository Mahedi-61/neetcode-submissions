class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        for i in range(0, 32):
            count += 1 if n & (1 << i) > 0 else 0

        return count