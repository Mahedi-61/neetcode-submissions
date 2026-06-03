class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if s == "": return 0

        i, j = 0, 1
        max_len = 1
        window = {s[i] : i}

        while j < len(s):
            if s[j] in window:
                max_len = max(max_len, j - i)
                i = window[s[j]] + 1
                keys = list(window.keys())
                for key in keys:
                    if window[key] < i:
                        del window[key]

            window.update({s[j] : j})
            j += 1
                
        max_len = max(max_len, j - i)
        return max_len