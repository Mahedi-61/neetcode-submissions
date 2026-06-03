class Solution:
    def find_palindrom(self, s):
        if len(s) < 2: return True
        if s[0] == s[-1]:
            return self.find_palindrom(s[1:-1])
        else:
            return False

    def check_alphnum(self, c):
        if (ord('A') <= ord(c) <= ord('Z') or 
            ord('a') <= ord(c) <= ord('z') or 
            ord('0') <= ord(c) <= ord('9')):
            return True
        else:
            return False 

    def isPalindrome(self, s: str) -> bool:
        i = 0
        j = len(s) - 1

        while(i < j):
            if not self.check_alphnum(s[i]):
                i = i + 1 
                continue
            
            if not self.check_alphnum(s[j]):
                j = j - 1 
                continue
          
            if s[i].lower() == s[j].lower():
                i += 1
                j -= 1 
            else: 
                return False 
        return True 