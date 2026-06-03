class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        #  z  x  y  z  x  y  z
        #(i,j)j  j (i,j)
        # (z) (z,x) (z,x,y) dict == {"alph":idx}
        # max_count = max(max_count, sub_count)

        #issue: updating dictionary: 
        if s == "": return 0

        dt_alpha = defaultdict(int)
        max_count = 0
        j = 0
        for i, c in enumerate(s):
            if c in dt_alpha and dt_alpha[c] >= j:
                sub_count = i - j
                j = dt_alpha[c] + 1
                max_count = max(max_count, sub_count)

            dt_alpha[c] = i
            
        return max(max_count, i - j + 1)
