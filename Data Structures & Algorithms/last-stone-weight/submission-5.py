class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        import heapq

        stones = [s*(-1) for s in stones]
        heapq.heapify(stones)
        while len(stones) > 1:
            a, b = heapq.heappop(stones), heapq.heappop(stones)
            if a != b:
                heapq.heappush(stones, a - b)

        return stones[0] * -1 if stones else 0