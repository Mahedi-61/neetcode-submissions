class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == "0" or num2 == "0":
            return "0"

        ls_muls = []
        for i, c2 in enumerate(num2[::-1]):
            
            a = int(c2)
            res = "" if i==0 else "0" * i
            carry = 0
            for c1 in num1[::-1]:
                total = int(c1) * a
                total += carry

                carry = total // 10
                res += str(total % 10)
            
            if carry: res += str(carry)
            ls_muls.append(res[::-1])

        if len(ls_muls) == 1: return ls_muls[0]
        size = len(ls_muls[-1])

        for i in range(len(ls_muls)):
            if len(ls_muls[i]) < size:
                ls_muls[i] = "0" * (size - len(ls_muls[i])) + ls_muls[i]

        carry = 0
        i = size - 1 
        res = ""

        while i >= 0 or carry:
            vals = [int(mul[i]) if i < len(mul) else 0 for mul in ls_muls]
            print(vals)
            total = sum(vals) + carry

            res += str(total % 10)
            carry = total // 10
            i -= 1

        return res[::-1]
