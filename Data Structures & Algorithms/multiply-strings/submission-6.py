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
            ls_muls.append(int(res[::-1]))

        return str(sum(ls_muls))