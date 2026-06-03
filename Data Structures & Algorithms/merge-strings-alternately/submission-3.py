class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        
        l, r = 0, 0
        result = ""

        while l < len(word1) or r < len(word2):
            c1 = word1[l] if l < len(word1) else ""
            c2 = word2[r] if r < len(word2) else ""
            
            result += c1 + c2

            l += 1
            r += 1

        return result