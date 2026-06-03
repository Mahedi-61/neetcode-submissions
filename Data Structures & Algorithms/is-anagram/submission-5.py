class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #without sorting
        dt_s = {}
        for c in s:
            if c in dt_s:
                dt_s[c] += 1
            else:
                dt_s[c] = 1

        dt_t = {}
        for c in t:
            if c in dt_t:
                dt_t[c] += 1
            else:
                dt_t[c] = 1

        return dt_t == dt_s
        