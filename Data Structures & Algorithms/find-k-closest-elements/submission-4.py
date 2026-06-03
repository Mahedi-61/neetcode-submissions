class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        #monotonically increasing stack
        
        stack = []

        for num in arr:
            dist = abs(x - num)

            if len(stack) < k:
                heapq.heappush(stack, [-dist, num])
            
            else:
                max_dist = -1 * stack[0][0]
                if dist < max_dist:
                    heapq.heappop(stack)
                    heapq.heappush(stack, [-dist, num])
        
        return sorted(i[1] for i in stack)
