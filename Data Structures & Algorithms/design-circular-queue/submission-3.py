class MyCircularQueue:
    def __init__(self, k: int):
        self.front = 0
        self.rear = 0
        self.k = k
        self.q = [-1] * k
        self.size = 0

    def enQueue(self, value: int) -> bool:
        if not self.isFull():
            self.q[self.rear] = value
            self.rear = (self.rear + 1) % self.k
            self.size += 1
            return True

        return False

    def deQueue(self) -> bool:
        if not self.isEmpty():
            self.q[self.front] = -1
            self.front = (self.front+1) % self.k
            self.size -= 1
            return True

        return False

    def Front(self) -> int:
        return self.q[self.front]

    def Rear(self) -> int:
        idx = (self.rear-1) % self.k
        return self.q[idx]

    def isEmpty(self) -> bool:
        return self.size == 0

    def isFull(self) -> bool:
        return self.size == self.k


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()