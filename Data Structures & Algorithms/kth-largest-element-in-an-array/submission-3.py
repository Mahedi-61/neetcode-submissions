class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # without sorting
        # max heap
        # maintaining fixed k size array; then the last value
        heap = []
        for num in nums:
            heapq.heappush(heap, num)
            if len(heap) > k:
                heapq.heappop(heap)

        return heapq.heappop(heap)