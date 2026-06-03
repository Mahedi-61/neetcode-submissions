class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        #memoization + recursion
        if amount == 0: return 0

        memo = {}
        def dfs(total):
            if total == 0:
                return 0
            if total < 0:
                return float("inf")

            if total in memo:
                return memo[total]

            min_val = float("inf")
            for c in coins:
                t_count = 1 + dfs(total - c)
                min_val = min(t_count, min_val)
            
            memo[total] = min_val
            return min_val

        dfs(amount)
        if amount not in memo or memo[amount] == float("inf"):
            return -1

        return memo[amount]