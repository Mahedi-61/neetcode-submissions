class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # brute-force solution O(n**2)
        max_profit = 0

        for i in range(len(prices) - 1):
            buy = prices[i]
            sell = max(prices[ i : ])
            if buy >= sell:
                profit = 0
            else:
                profit = sell - buy

            max_profit = max( max_profit, profit)
        return max_profit 