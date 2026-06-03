class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        temp = strs[0]
        j = 0

        while len(temp) >= j + 1: 
            for i in range(1, len(strs)):
                if len(strs[i]) >= j + 1 and strs[i][j] == temp[j]:
                    continue

                else:
                    return temp[ : j]

            j += 1

        return temp