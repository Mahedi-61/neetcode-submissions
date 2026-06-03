class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        if left == 0: return 0

        diff = right - left
        n = right
        res = 0
        i = 0

        while n:
            if diff < (1 << i):
                temp = ((left >> i) & 1) & ((right >> i) & 1)
                if temp:
                    res |= (temp << i)

            i += 1
            n = n >> 1
        return res