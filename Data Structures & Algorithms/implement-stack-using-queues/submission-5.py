class MyStack:
    def __init__(self):
        self.in_queue = deque([])
        self.out_queue = deque([])
        
    def push(self, x: int) -> None:
        self.in_queue.append(x)
        
    def pop(self) -> int:
        self.top()
        return self.out_queue.popleft()

    def top(self) -> int:
        if self.in_queue:
            for _ in range(len(self.in_queue)):
                self.out_queue.appendleft(self.in_queue.popleft())

        return self.out_queue[0]

    def empty(self) -> bool:
        return max(len(self.in_queue), len(self.out_queue)) == 0

# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()