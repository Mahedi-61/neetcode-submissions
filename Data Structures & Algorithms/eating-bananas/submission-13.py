class Solution:
    import math 
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        if len(piles) == 1: return math.ceil(piles[0] / h)
        h_rate = max(piles)

        def find_hour(rate):
            hour = 0
            for p in piles:
                hour += math.ceil(p / rate)
            return hour 

        #binary search
        h_rate = max(piles) #h_rate --reuqire minimum possible time
        l_rate = 1 #l_rate -- require maximum possible time

        while l_rate < h_rate:
            mid_rate = (l_rate + h_rate) // 2
            mid_hour = find_hour(mid_rate)

            if h >= mid_hour:
                h_rate = mid_rate
            else:
                l_rate = mid_rate + 1

        return l_rate

