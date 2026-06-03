class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        i, j = 0, 0
        res = ""
        while i < len(word1) or j < len(word2):
            res += word1[i] if i < len(word1) else ""
            res += word2[j] if j < len(word2) else ""

            i += 1
            j += 1
        return res