class Solution:
    def addBinary(self, a: str, b: str) -> str:
        res = ""
        carry = 0
        a = int(a, 2) #binary string converted to int
        b = int(b, 2)

        if a == 0 and b == 0: return str(0)

        while a or b or carry:

            a_digit = 0
            if a != 0 and (a ^ 1) % 2 == 0:
                a_digit = 1 

            b_digit = 0
            if b != 0 and (b ^ 1) % 2 == 0:
                b_digit = 1 

            total = a_digit + b_digit + carry
            if total == 2:
                total = 0
                carry = 1

            elif total == 3:
                total = 1
                carry = 1
            else:
                carry = 0

            res += str(total)
            a = a >> 1
            b = b >> 1

        return res[::-1]