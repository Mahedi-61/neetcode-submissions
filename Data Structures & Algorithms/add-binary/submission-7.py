class Solution:
    def addBinary(self, a: str, b: str) -> str:
        # Technique 1: convert binary to int
        # adding int; then convert it to binary
        i = 0
        carry = 0
        res = []

        a = a[::-1]
        b = b[::-1]

        while i < len(a) or i < len(b) or carry:
            x = int(a[i]) if i < len(a) else 0
            y = int(b[i]) if i < len(b) else 0

            temp_sum = x + y + carry
            if temp_sum == 2:
                carry = 1
                res.append('0')

            elif temp_sum == 3:
                carry = 1
                res.append('1')
            else:
                carry = 0
                res.append(str(temp_sum))

            i += 1

        return "".join(res[::-1])
