class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        from collections import Counter
        #sliding window problem
        set_s1 = set(s1)
        l,r = 0, 0
        
        def check(s):
            return Counter(s) == Counter(s1)
            
        while r < len(s2):
            if s2[r] in set_s1:
                r += 1
                sub_string = s2[l : r]

                if len(sub_string) == len(s1):
                    if check(sub_string): 
                        return True 
                    else:
                        l += 1
            else:
                r += 1
                l = r

        return False