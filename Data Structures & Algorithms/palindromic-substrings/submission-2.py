class Solution:
    def countSubstrings(self, s: str) -> int:
        def is_palindrom(s):
            l = 0
            r = len(s) - 1
            while l <= r:
                if s[l] != s[r]:
                    return False
                l += 1
                r -= 1
            return True

        res = len(s)
        k = 1
        while k < len(s):
            for i in range(len(s)-k):
                if is_palindrom(s[i : i+k+1]):
                    res += 1
            k += 1
        return res