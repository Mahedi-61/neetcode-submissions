class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # greedy
        # dp (bottom-up + space optimized)
        # recursive + memoization

        dp = [0] * (len(cost) + 1)
        dp[2] = min(cost[1], cost[0])

        for i in range(3, len(cost) + 1):
            dp[i] = min(cost[i-2] + dp[i-2], cost[i-1] + dp[i-1])
            
        return dp[len(cost)]
        