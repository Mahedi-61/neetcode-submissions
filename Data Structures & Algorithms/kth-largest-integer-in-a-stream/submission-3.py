from heapq import heapify, heappush, heappop
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.nums = nums
        self.k = k
        self.heap = sorted(self.nums)[-k:]
        heapify(self.heap)

    def add(self, val: int) -> int:
        self.nums.append(val)
        heappush(self.heap, val)
        if len(self.heap) > self.k: heappop(self.heap)
        return self.heap[0] if len(self.heap) == self.k else None
        
