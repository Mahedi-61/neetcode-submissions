class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        i, j = 0, 0
        res = ""
        while i < len(word1) or j < len(word2):
            f = word1[i] if i < len(word1) else ""
            s = word2[j] if j < len(word2) else ""
            i += 1
            j += 1
            res += f + s

        return res