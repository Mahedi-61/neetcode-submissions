class MyStack:
    def __init__(self):
        self.in_queue = collections.deque([])
        self.out_queue = collections.deque([])
        
    def push(self, x: int) -> None:
        self.in_queue.append(x)   

    def pop(self) -> int:
        while self.in_queue:
            self.out_queue.append(self.in_queue.pop())

        if self.out_queue:
            return self.out_queue.popleft()   
        return None         

    def top(self) -> int:
        if self.in_queue:
            return self.in_queue[-1]
        elif self.out_queue:
            return self.out_queue[0]
        else:
            return None

    def empty(self) -> bool:
        l = len(self.in_queue) + len(self.out_queue)
        return l == 0

# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()