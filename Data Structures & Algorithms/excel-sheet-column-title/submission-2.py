class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        num = columnNumber
        res = []

        while num > 0:
            remainder = num % 26
            num = num // 26
            if remainder == 0:
                num -= 1
                res.append("Z")

            else:
                res.append(chr( ord("A") + remainder - 1))

        return "".join(res[::-1])
