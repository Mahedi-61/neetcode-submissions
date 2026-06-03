class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0: return 0
        
        #top-down recursion with memoization
        def dfs(total):
            if total == 0:
                return 0

            if total in memo:
                return memo[total]

            min_val = float("inf")
            for c in coins:
                if total - c >= 0:
                    min_val = min(min_val, 1 + dfs(total-c))

            memo[total] = min_val
            return memo[total]

        memo = {}
        dfs(amount)
        return memo[amount] if memo[amount] < float("inf") else -1 