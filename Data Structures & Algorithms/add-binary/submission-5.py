class Solution:
    def addBinary(self, a: str, b: str) -> str:
        i = 0 
        j = 0

        res = ""
        carry = 0
        a = a[::-1]
        b = b[::-1]

        while i < len(a) and j < len(b):
            add = int(a[i]) + int(b[j]) + carry
            res += str(add % 2)
            carry = add // 2
            i += 1
            j += 1

        while i < len(a):
            add = int(a[i]) + carry
            res += str(add % 2)
            carry = add // 2
            i += 1

        while j < len(b):
            add = int(b[j]) + carry
            res += str(add % 2)
            carry = add // 2
            j += 1

        if carry == 1:
            res += "1"
        return res[::-1]