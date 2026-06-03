class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        """
        #brute-force
        result = ""
        i = 0 
        while(True):
            for in_str in strs:
                if i==0 and len(in_str) == 0: return ""
                if i < len(in_str) and in_str[i] ==  strs[0][i]:
                    pass 
                else:
                    return result 
            
            result +=  strs[0][i]
            i+= 1

        return result  
        """
        temp = strs[0]
        if len(temp) == 0: return ""

        for i in range(1, len(strs)):
            if len(strs[i]) == 0: return ""

            while temp not in strs[i]:
                temp = temp[:-1]

            if temp == "": return temp
            
        return temp 

