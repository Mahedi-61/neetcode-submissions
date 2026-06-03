class Solution:
    def do_check(self, s):
        if len(s) < 2: return True 
        if s[0] != s[-1]: return False
        return self.do_check(s[1:-1])


    def validPalindrome(self, s: str) -> bool:

        l = 0
        r = len(s) - 1

        while l < r:
            if s[l] != s[r]:
                skip_left = s[l + 1 : r + 1]
                skip_right = s[l : r]
                return self.do_check(skip_left) or self.do_check(skip_right)

            l += 1
            r -= 1
        return True 