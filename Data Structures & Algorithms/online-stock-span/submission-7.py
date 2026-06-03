class StockSpanner:
    def __init__(self):
        self.stack = []
        
    def next(self, price: int) -> int:
        count = 1
        i = 0
        if self.stack:
            while i < len(self.stack) and self.stack[len(self.stack)-1 - i] <= price:
                i += 1

        self.stack.append(price)
        return count + i