class MyStack:
    def __init__(self):
        self.in_queue = deque([])
        
    def push(self, x: int) -> None:
        self.in_queue.append(x)   
        for _ in range(len(self.in_queue) - 1):
            self.in_queue.append(self.in_queue.popleft())

    def pop(self) -> int:
        return self.in_queue.popleft()

    def top(self) -> int:
        if self.in_queue:
            return self.in_queue[0]
        return None

    def empty(self) -> bool:
        return len(self.in_queue) == 0

# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()