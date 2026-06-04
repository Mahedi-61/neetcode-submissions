class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        ls_s = [0] * 26
        ls_t = [0] * 26

        for c in s:
            c_idx = ord(c) - ord('a')
            ls_s[c_idx] += 1

        for c in t:
            c_idx = ord(c) - ord('a')
            ls_t[c_idx] += 1

        return ls_s == ls_t