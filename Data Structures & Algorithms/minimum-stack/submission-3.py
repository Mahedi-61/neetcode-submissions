class MinStack:
    import heapq

    def __init__(self):
        self.min_stack = []
        self.temp_stack = []

    def push(self, val: int) -> None:
        self.min_stack.append(val)
        self.temp_stack.append(min(val, self.temp_stack[-1] if self.temp_stack else val))

    def pop(self) -> None:
        self.min_stack.pop()
        self.temp_stack.pop()

    def top(self) -> int:
        return self.min_stack[-1]

    def getMin(self) -> int:
        return self.temp_stack[-1]
        
