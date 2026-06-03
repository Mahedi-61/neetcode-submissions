class MyQueue:
    def __init__(self):
        self.push_stack = []
        self.pop_stack = []

    def push(self, x: int) -> None:
        if not self.pop_stack:
            self.pop_stack.append(x)

        else:
            for _ in range(len(self.pop_stack)):
                self.push_stack.append(self.pop_stack.pop())
            self.push_stack.append(x)
            for _ in range(len(self.push_stack)):
                self.pop_stack.append(self.push_stack.pop())

    def pop(self) -> int:
        return self.pop_stack.pop()

    def peek(self) -> int:
        return self.pop_stack[-1]

    def empty(self) -> bool:
        return len(self.pop_stack) == 0

# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()