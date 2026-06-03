class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        import heapq
        self.nums = nums
        self.k = k
        heapq.heapify(self.nums)

    def add(self, val: int) -> int:
        heapq.heappush(self.nums, val)

        for _ in range(len(self.nums)-1, self.k-1, -1):
            heapq.heappop(self.nums)

        return self.nums[0]