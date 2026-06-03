class Solution:
    def do_check(self, s):
        l = 0
        r = len(s) - 1
        while l < r:
            if s[l] != s[r]:
                return False

            l, r = l+1, r-1
        return True


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