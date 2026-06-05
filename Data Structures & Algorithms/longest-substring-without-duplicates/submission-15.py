class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if s == "": return 0

        dict_alpha = defaultdict(int)
        max_count = 1
        j = 0 

        for i, c in enumerate(s):
            if c in dict_alpha and dict_alpha[c] >= j:
                
                max_count = max(max_count, i - j)
                j = dict_alpha[c] + 1
            
            dict_alpha[c] = i

        return max(max_count, i - j + 1)