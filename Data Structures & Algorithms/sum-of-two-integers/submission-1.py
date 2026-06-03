class Solution:
    def getSum(self, a: int, b: int) -> int:
        res = 0
        carry = 0

        if a < 0:
            a = (1 << 32) + a

        if b < 0:
            b = (1 << 32) + b

        for i in range(32):
            bit_a =  1 if a & (1 << i) else 0
            bit_b = 1 if b & (1 << i) else 0
            res |= (bit_a ^ bit_b ^ carry) << i
            carry = (bit_a & bit_b) | (bit_b & carry) | (bit_a & carry)

        # if carry:
        #     res |= (1 << 32)

        if res >= (1 << 31):  # MSB is 1 → negative number
            res -= (1 << 32)
        return res