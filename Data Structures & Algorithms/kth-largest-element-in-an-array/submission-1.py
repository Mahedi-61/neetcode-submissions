class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        #without sorting

        heapq.heapify(nums)
        for _ in range(len(nums)-1, k-1 ,-1):
            heapq.heappop(nums)

        return nums[0]
        