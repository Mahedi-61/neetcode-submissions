class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        
        def dfs(idx1, idx2, memo):
            if idx1 >= len(text1) or idx2 >=len(text2):
                return 0
                
            if (idx1, idx2) in memo:
                return memo[(idx1, idx2)]

            if text1[idx1] == text2[idx2]:
                idx1 += 1
                idx2 += 1
                return 1 + dfs(idx1, idx2, memo)
                
            memo[(idx1, idx2)] = max(dfs(idx1+1, idx2, memo), dfs(idx1, idx2+1, memo))
            return memo[(idx1, idx2)]

        return dfs(0, 0, memo={})