class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        num = columnNumber
        res = []
        alph_dict = {i + 1 : chr(ch_num) for i, ch_num in enumerate(range(65, 91))}

        while num > 0:
            remainder = num % 26
            num = num // 26
            if remainder == 0:
                num -= 1
                res.append(alph_dict[26])

            else:
                res.append(alph_dict[remainder])

        return "".join(res[::-1])
