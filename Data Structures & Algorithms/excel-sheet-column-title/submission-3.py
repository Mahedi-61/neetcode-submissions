class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        dict_chars = {i : chr(ord("A") - 1 + i) for i in range(1, 27)}

        res = ""
        while columnNumber:
            columnNumber -= 1
            temp = columnNumber % 26

            columnNumber //= 26
            res += dict_chars[temp + 1]

        return res[::-1]