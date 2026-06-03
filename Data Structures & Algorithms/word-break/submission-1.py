class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        #dp with top-down approach
        wordDict = [list(w) for w in wordDict]
        ls_s = list(s)
        memo = {}

        def dfs(ls_s):
            if len(ls_s) == 0:
                return True
            
            if "".join(ls_s) in memo:
                return memo["".join(ls_s)]

            gl_status = False
            for w in wordDict:
                if len(ls_s) >= len(w) and ls_s[-len(w) : ] == w:
                    status = dfs(ls_s[ : len(ls_s)- len(w)])
                    gl_status = gl_status or status

            memo["".join(ls_s)] = gl_status
            return gl_status

        return dfs(list(s))
    
