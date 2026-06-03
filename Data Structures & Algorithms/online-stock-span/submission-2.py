class StockSpanner:

    def __init__(self):
        self.stock = []
    # Returns the span of the stock's price given that today's price
    # where the stock price was less than or equal to the price of that day.
    # the maximum number of consecutive days 
    def next(self, price: int) -> int:
        count = 1
        while self.stock and self.stock[-1 * count] <= price:
            count += 1
            if count - len(self.stock) > 0: break

        self.stock.append(price)
        return count 

# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)
