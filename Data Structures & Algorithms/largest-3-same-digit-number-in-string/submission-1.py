class Solution:
    def largestGoodInteger(self, num: str) -> str:
        i = 0
        max_num = float('-inf')

        while i < len(num)-2:
            if num[i] == num[i+1] == num[i+2]:
                max_num = max(max_num, int(num[i : i+3]))

            i += 1

        if max_num == float('-inf'): return ""
        elif max_num == 0: return "000"
        return str(max_num)