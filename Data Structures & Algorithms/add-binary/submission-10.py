class Solution:
    def addBinary(self, a: str, b: str) -> str:
        res = ""
        carry = 0
        i = 0
        a = a[::-1]
        b = b[::-1]

        while i < len(a) or i < len(b) or carry:
            digit_a = int(a[i]) if i < len(a) else 0
            digit_b = int(b[i]) if i < len(b) else 0

            total = carry + digit_a + digit_b
            if total == 3:
                total = 1
                carry = 1
                
            elif total == 2:
                total = 0
                carry = 1
            else:
                carry = 0

            res += str(total)
            i += 1
        
        return res[::-1]