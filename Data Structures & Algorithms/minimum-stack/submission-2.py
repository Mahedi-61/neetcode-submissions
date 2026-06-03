class MinStack:
    import heapq

    def __init__(self):
        self.min_stack = []
        self.min_heap = []

    def push(self, val: int) -> None:
        self.min_stack.append(val)
        heapq.heappush(self.min_heap, val)

    def pop(self) -> None:
        self.min_heap.remove(self.min_stack.pop()) 
        heapq.heapify(self.min_heap)

    def top(self) -> int:
        return self.min_stack[-1]

    def getMin(self) -> int:
        print(self.min_heap)
        return self.min_heap[0]
        
