class Solution:
    def hammingWeight(self, n: int) -> int:
        #return n.bit_count()
        count = 0
        for i in range(32):
            if n & (1 << i) > 0:
                count += 1

        return count 
        