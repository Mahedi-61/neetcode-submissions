class Solution:
    def countSubstrings(self, s: str) -> int:
        def is_palindrom(l, r):
            count = 0
            while l >= 0 and r < len(s):
                    if s[l] != s[r]:
                        return count
                    l -= 1
                    r += 1
                    count += 1
            return count

        res = 0
        for i in range(len(s)):
            res += is_palindrom(i, i)
            res += is_palindrom(i, i+1)

        return res