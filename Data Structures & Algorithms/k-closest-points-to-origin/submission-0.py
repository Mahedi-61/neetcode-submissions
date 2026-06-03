from heapq import heapify, heappop
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distance_dict = {}
        for p in points:
            distance = (p[0]**2 + p[1]**2) ** 0.5
            distance_dict[distance] = [p] + distance_dict.get(distance, [])

            min_heap = list(distance_dict.keys())
            heapify(min_heap)

        result = []
        while k  > 0:
            key = heappop(min_heap)
            points = distance_dict[key]
            result += points
            k -= len(points)

        return result
        