class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        #adaptive sliding window
        dt_count = {}
        long_str = 0
        l, r = 0, 0

        while r < len(s):
            if s[r] in dt_count:
                dt_count[s[r]] += 1
            else:
                dt_count[s[r]] = 1
 
            while (r - l + 1) - max(dt_count.values()) > k:
                dt_count[s[l]] -= 1
                l += 1

            long_str = max(long_str, r - l + 1)
            r += 1 

        return long_str