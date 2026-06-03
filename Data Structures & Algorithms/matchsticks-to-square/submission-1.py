class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        if len(matchsticks) < 4:
            return False

        total = sum(matchsticks) 
        if  total % 4 != 0:
            return False

        matchsticks.sort(reverse=True)
        side = total // 4
        if any (num > side for num in matchsticks):
            return False

        def dfs(idx):
            if idx == len(matchsticks):
                return all(s==side for s in dp)

            for i in range(4):
                if i > 0 and dp[i-1] == dp[i]:
                    continue

                if dp[i] + matchsticks[idx] <= side:
                    dp[i] += matchsticks[idx]

                    if dfs(idx + 1):
                        return True
                    
                    dp[i] -= matchsticks[idx]

            return False

        dp = [0] * 4
        return dfs(0)
