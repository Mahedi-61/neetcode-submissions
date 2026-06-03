class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_buy = prices[0]
        max_profit = 0

        for p in prices:
            if p < min_buy:
                min_buy = p
            max_profit = max(max_profit, p - min_buy)

        return max_profit
