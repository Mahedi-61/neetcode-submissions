class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # find the length of the longest substring without duplicate characters.
        # Brute force (two pointer approach)
        i = 0
        res = 0

        while i < len(s):
            j = i
            char_set = set()
            
            while j < len(s) and s[j] not in char_set:
                char_set.add(s[j])
                j += 1
            
            res = max(res, len(char_set))
            i += 1
        return res