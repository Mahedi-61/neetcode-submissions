class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        def dfs(i):
            if len(s) == i:
                return True
            if i in memo:
                return memo[i]

            for word in wordDict:
                if s[i: i + len(word)] == word:
                    status = dfs(i + len(word))
                    if status: return True
                    
            memo[i] = False
            return False

        memo = {}
        return dfs(0)