import functools
class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        # 2 dimensional DP
        
        @functools.cache
        def dfs(i, j):
            left, right = False, False
            if i + j == len(s3):
                return True

            # elif i + j in memo:
            #     return memo[i+j]

            if i < len(s1) and s1[i] == s3[i+j]:
                left = dfs(i+1, j)

            if j < len(s2) and s2[j] == s3[i+j]:
                right = dfs(i, j+1)

            #memo[i+j] = left or right
            return left or right #memo[i+j]


        if len(s1) + len(s2) != len(s3):
            return False

        memo = {}
        return dfs(0, 0)
