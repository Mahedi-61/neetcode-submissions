class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # find the length of the longest substring without duplicate characters.
        # Brute force (two pointer approach)

        # optimized solution (sliding window)
        i = 0
        res = 0
        char_set = set()
        j = 0
        while i < len(s):
            if s[i] in char_set:
                print(s[j : i])
                res = max(res, i - j)
                while j < len(s) and s[j] != s[i]:
                    char_set.discard(s[j])
                    j += 1
                j += 1

            char_set.add(s[i])
            i += 1

        res = max(res, i - j)
        return res
