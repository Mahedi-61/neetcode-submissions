class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        #adaptive sliding window
        dt_count = {}
        long_str = 0
        max_freq = 0
        l, r = 0, 0

        while r < len(s):
            dt_count[s[r]] = dt_count.get(s[r], 0) + 1
            max_freq = max(max_freq, dt_count[s[r]])

            if (r - l + 1) - max_freq > k:
                dt_count[s[l]] -= 1
                l += 1

            long_str = max(long_str, r - l + 1)
            r += 1 

        return long_str