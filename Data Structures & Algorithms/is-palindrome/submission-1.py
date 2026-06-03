class Solution:
    def find_palindrom(self, s):
        if len(s) < 2: return True
        if s[0] == s[-1]:
            return self.find_palindrom(s[1:-1])
        else:
            return False

    def isPalindrome(self, s: str) -> bool:
        s = "".join([ch for ch in s if ch.isalnum()])
        s = s.lower()

        i = 0
        j = len(s) - 1
        while(i < j):
            if s[i] == s[j]:
                i += 1
                j -= 1 
            else: return False 
        return True 