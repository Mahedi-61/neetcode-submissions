class MyStack:

    def __init__(self):
        self.q1 = []
        self.q2 = []
        self.length = 0

    def push(self, x: int) -> None:
        while len(self.q2) != 0:
            self.q1.append(self.q2.pop())

        self.q1.append(x)

        while len(self.q1) != 0:
            self.q2.append(self.q1.pop())
        self.length += 1

    def pop(self) -> int:
        if self.length != 0:
            temp = self.q2[0]
            self.length -= 1
            del self.q2[0]
            return temp 
        else:
            return None

    def top(self) -> int:
        return self.q2[0]

    def empty(self) -> bool:
        return self.length == 0


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()