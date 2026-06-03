class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        heapq.heapify(heap)

        for p in points:
            dist = math.sqrt(p[0]**2 + p[1]**2)
            heapq.heappush(heap, (-dist, p[0], p[1]))

            if len(heap) > k:
                heapq.heappop(heap)

        return [[p[1], p[2]] for p in heap]