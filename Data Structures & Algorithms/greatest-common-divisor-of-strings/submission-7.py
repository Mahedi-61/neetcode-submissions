class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if str1 + str2 == str2 + str1: 
            max_len = min(len(str1), len(str2))

            for length in range(max_len, 0, -1):
                if len(str1) % length == 0 and len(str2) % length == 0:
                    return str1[:length]
        return ""