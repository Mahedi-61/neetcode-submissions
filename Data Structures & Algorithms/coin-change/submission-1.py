class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # backtracking + memoization + recursion
        if amount == 0: return 0
        memo = {}

        def dfs(total):
            if total == 0:
                return 0

            elif total < 0:
                return 10000

            if total in memo:
                return memo[total]

            min_count = 10000
            for c in coins:
                min_val = 1 + dfs(total-c)
                min_count = min(min_val, min_count)

            memo[total] = min_count
            return min_count

        dfs(amount)
        if amount not in memo or memo[amount] == 10000:
            return -1
        
        return memo[amount] 