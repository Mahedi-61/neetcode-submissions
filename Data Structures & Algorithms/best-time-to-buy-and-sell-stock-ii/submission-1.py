class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        stock = prices[0]

        for p in prices:
            if p > stock:
                max_profit += (p - stock)
            stock = p

        return max_profit

