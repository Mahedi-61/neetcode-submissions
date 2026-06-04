class Solution:
    def validPalindrome(self, s: str) -> bool:
        
        def check(s):
            if len(s) < 1:
                return True

            if s[0] == s[-1]:
                return check(s[1:-1])
            else:
                return False

        l, r = 0, len(s)-1
        while l < r:
            if s[l] == s[r]:
                l += 1
                r -= 1
            else:
                return check(s[l+1:r+1]) or check(s[l:r]) 
                
        return True