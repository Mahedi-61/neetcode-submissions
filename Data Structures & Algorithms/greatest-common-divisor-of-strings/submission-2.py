class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if str1 == str2: return str1 

        res = ""
        if len(str1) == len(str2):
            return res
        
        elif len(str1) > len(str2):
            max_str = ""
            for i in range(1, len(str1)//2 + 1):
                res = str1[ : i]
                temp = res
                status = True
                while len(temp) < len(str1)  + len(res):
                    if temp in str1:
                        temp += res
                    else:
                        status = False
                        break

                temp = res
                while status == True and len(temp) < len(str2) + len(res):
                    if temp in str2:
                        temp += res
                    else:
                        status = False
                        break 

                if status == True:
                    max_str = res
   
        else:
            max_str = ""
            for i in range(1, len(str2)//2 + 1):
                res = str2[ : i]
                temp = res
                status = True
                while len(temp) < len(str2)  + len(res):
                    if temp in str2:
                        temp += res
                    else:
                        status = False
                        break
 
                temp = res
                while status == True and len(temp) < len(str1)  + len(res):
                    if temp in str1:
                        temp += res
                    else:
                        status = False
                        break 

                if status == True:
                    max_str = res
 
        return max_str

