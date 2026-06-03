class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        str_dict = {}

        # first string (s) -- hash table 
        for c in s:
            if c in str_dict:
                str_dict[c] += 1
            else:
                str_dict[c] = 1 

        for ch in t:
            if ch in str_dict and str_dict[ch] > 0:
                str_dict[ch] -= 1 
            else:
                return False 

        return True if sum(list(str_dict.values())) == 0 else False       
        