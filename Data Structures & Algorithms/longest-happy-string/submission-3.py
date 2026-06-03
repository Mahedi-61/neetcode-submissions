class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        # heap = [freq_a: a, freq_b: b, freq_c: c]
        heap = []
        heapq.heapify(heap)

        for f, char in [(a, "a"), (b, "b"), (c, "c")]:
            if f > 0:
                heapq.heappush(heap, (-f, char))

        res = ""
        while heap:
            freq, char = heapq.heappop(heap)
            freq = abs(freq)
            freq -= 1

            if res[-2:] in ["aa", "bb", "cc"] and char == res[-1]:
                if heap:
                    freq_2, char_2 = heapq.heappop(heap)
                    res += char_2
                    freq_2 = abs(freq_2)
                    freq_2 -= 1

                    if freq_2 > 0:
                        heapq.heappush(heap, (-freq_2, char_2))
                else:
                    return res
            
            res += char
            if freq > 0:
                heapq.heappush(heap, (-freq, char))
        return res