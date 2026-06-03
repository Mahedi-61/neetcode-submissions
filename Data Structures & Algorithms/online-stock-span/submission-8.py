class StockSpanner:
    def __init__(self):
        self.stack = []
        
    #[100], [80], [60], [70], [60], [75], [85]
    #[[100, 0], [85, 5]]
    def next(self, price: int) -> int:
        t_span = 0 
        while self.stack and self.stack[-1][0] <= price:
            last_price, span = self.stack.pop()
            t_span += (span + 1)

        self.stack.append([price, t_span])
        return t_span + 1

    # problem of monotonically decreasing stack
    # cause it says consecutive days 
    # so we don't need to store values which are lower than today's stock 
    # that's help us to remove O(n**2)
    # it also gives clue to make decreasing stack.
    # as we are removing some of the stocks values we need to store the span