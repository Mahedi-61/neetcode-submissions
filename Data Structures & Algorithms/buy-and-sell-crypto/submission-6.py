class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #maximum profit you can achieve
        max_profit = 0
        min_buy = prices[0]
        if len(prices) < 2: return max_profit

        for idx in range(1, len(prices)):
            max_profit = max(max_profit, prices[idx] - min_buy)
            min_buy = min(min_buy, prices[idx])

        return max_profit