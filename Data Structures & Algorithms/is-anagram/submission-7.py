class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Solution 3
        s_key = [0] * 26
        t_key = [0] * 26
        for c in s:
            s_key[ord(c) - ord("a")] += 1

        for c in t:
            t_key[ord(c) - ord("a")] += 1

        return s_key == t_key 