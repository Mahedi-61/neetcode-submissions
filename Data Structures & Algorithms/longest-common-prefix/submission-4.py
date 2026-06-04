class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        res = ""
        i = 0

        while i < len(strs[0]):
            c = strs[0][i]
            
            for word in strs[1:]:
                test_c = word[i] if i < len(word) else ""
                if c != test_c:
                    return res

            res += c
            i += 1

        return res