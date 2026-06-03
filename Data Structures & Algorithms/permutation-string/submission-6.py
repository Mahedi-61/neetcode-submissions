class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        ls_s1 = [0] * 26
        ls_s2 = [0] * 26

        for c in s1:
            ls_s1[ord(c) - ord("a")] += 1 

        for c in s2[ : len(s1)]:
            ls_s2[ord(c) - ord("a")] += 1 

        i, j = 0, len(s1)
        while j < len(s2):
            if ls_s1 == ls_s2:
                return True
            
            else:
                ls_s2[ord(s2[i]) - ord("a")] -= 1
                ls_s2[ord(s2[j]) - ord("a")] += 1
                i += 1
                j += 1
                
        return ls_s1 == ls_s2

