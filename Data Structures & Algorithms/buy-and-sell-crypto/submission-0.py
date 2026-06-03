class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # brute-force solution
        max_profit = 0
        if len(prices) == 1: return max_profit

        for i in range(len(prices) - 1):
            buy = prices[i]
            sell = max(prices[ i+1 : ])
            profit = 0 if buy >= sell else sell-buy
            max_profit = max(max_profit, profit)

        return max_profit