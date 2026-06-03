class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # can hold at most one share of the stock at any time.
        # On each day, you may decide to buy and/or sell the stock. 
        # Find and return the maximum profit you can achieve.

        # can't sort
        # find max and min to get large profit multiple times

        i = 0
        profit = 0

        while i < len(prices) - 1:
            j = i + 1 
            if j < len(prices) and prices[i] < prices[j]:
                profit += prices[j] - prices[i]

            i += 1
        return profit
