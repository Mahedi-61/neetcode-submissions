class Solution:
    def getSum(self, a: int, b: int) -> int:
        carry = 0
        res = 0
        mask = 0xFFFFFFFF

        for i in range(32):
            digit_a = ((a >> i) & 1)
            digit_b = ((b >> i) & 1)
            total = digit_a ^ digit_b ^ carry
            if total:
                res |= (1 << i)

            carry = int((digit_a + digit_b + carry) > 1)

        if res > 0x7FFFFFFF:
            res = ~(res ^ mask)

        return res