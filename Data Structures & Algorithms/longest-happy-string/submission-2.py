import heapq

class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        heap = []
        if a != 0:  heap.append((-a, "a"))
        if b != 0:  heap.append((-b, "b"))
        if c != 0:  heap.append((-c, "c"))

        heapq.heapify(heap)

        res = ''
        while heap:
            temp = heapq.heappop(heap)
            freq, char = temp

            if len(res) >= 1:
                if res[-2:] + char in ['aaa', 'bbb', 'ccc']:
                    if heap:
                        freq1, char1 = heapq.heappop(heap)
                        heapq.heappush(heap, temp)
                        freq, char = freq1, char1
                    else:
                        return res 

            res += char
            freq = abs(freq) - 1
            if freq > 0:
                again = (-freq, char)
                heapq.heappush(heap, again)
            
        return res 