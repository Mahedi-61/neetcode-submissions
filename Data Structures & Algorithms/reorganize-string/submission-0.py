import heapq
class Solution:
    def reorganizeString(self, s: str) -> str:
        char_dict = defaultdict(int)
        for c in s:
            char_dict[c] += 1

        heap = []
        for key in char_dict:
            heapq.heappush(heap, (-1 * char_dict[key], key))

        res = ""
        char_set = tuple()

        while heap:
            freq, c = heapq.heappop(heap)
            res += c

            if char_set:
                heapq.heappush(heap, char_set)
                char_set = tuple()

            freq = abs(freq) - 1
            if freq > 0:
                char_set = (-freq, c)

        print(res, char_set)
        if char_set == ():
            return res  
        else:
            return ""

