class Solution:
    def isPalindrome(self, s: str) -> bool:
        res = [chr(i) for i in range(65, 91)]
        res += [chr(i) for i in range(48, 58)]
        res += [chr(i) for i in range(97, 123)]
        
        final_string = []
        for c in s:
            if c in res:
                final_string.append(c.lower())


        l, r = 0, len(final_string) - 1

        while l <= r:
            if final_string[l] == final_string[r]:
                l += 1
                r -= 1
            else:
                return False

        return True