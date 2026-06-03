class Solution:
    def check_front(self, s, first):
        if len(s) < 2: return True 
        if s[0] != s[len(s)- 1]:
            if not first:
                if s[1] == s[len(s) - 1]:
                    first = True
                    return self.check_front(s[2 : len(s)-1], first)
                else:
                    return False
            else:
                return False
        return self.check_front(s[1 : len(s)-1], first)  

    def check_back(self, s, first):
        if len(s) < 2: return True 
        if s[0] != s[len(s)- 1]:
            if not first:
                if s[0] == s[len(s) - 2]:
                    first = True
                    return self.check_back(s[1 : len(s)-2], first)
                else:
                    return False
            else:
                return False
        return self.check_back(s[1 : len(s)-1], first) 


    def validPalindrome(self, s: str) -> bool:
        if len(s) < 2: return True 
        if s[0] != s[len(s)- 1]:
            s2 = s
            sami = self.check_front(s, first = False) 
            meraj = self.check_back(s2, first = False)
            print(sami, meraj)
            return sami or meraj

        return self.validPalindrome(s[1 : len(s)-1])

    #two pointer approach
    # def validPalindrome(self, s: str) -> bool:
    #     i = 0
    #     j = len(s) - 1
    #     del_one = False

    #     while i < j:
    #         if s[i] != s[j]:
    #             if not del_one:
    #                 if s[i + 1] == s[j]:
    #                     del_one = True
    #                     i += 1
    #                     continue

    #                 if s[i] == s[j - 1]:
    #                     del_one = True
    #                     j -= 1
    #                     continue
    #                 else:
    #                     return False
    #             else:
    #                 return False 
            
    #         i += 1
    #         j -= 1
    #     return True