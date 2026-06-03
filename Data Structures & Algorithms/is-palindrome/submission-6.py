class Solution:
    def isPalindrome(self, s: str) -> bool:
        res = [chr(i) for i in range(65, 91)]
        res += [chr(i) for i in range(48, 58)]
        res += [chr(i) for i in range(97, 123)]

        final_s = []
        for c in s:
            if c in res:
                final_s.append(c.lower())
        
        def check_palindrom(s):
            if len(s) < 2:
                return True

            if s[0] == s[-1]:
                return check_palindrom(s[1:-1])

            else:
                return False

        return check_palindrom(final_s)