class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # find the length of the longest substring without duplicate characters.
        # Brute force (two pointer approach) O(n**2)
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

        # optimized solution (sliding window)
        i = 0
        char_set = set()
        res = 0

        while i < len(s):

            if s[i] in char_set:
                res = max(res, i - j)

                while j < len(s) and s[j] != s[i]:
                    char_set.discard(s[j])
                    j += 1
                j += 1
                
        res = max(res, i - j)
        i += 1
        return res 