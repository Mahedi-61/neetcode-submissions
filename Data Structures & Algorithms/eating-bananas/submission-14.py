class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        import math 

        def find_hour_with_rate(k):
            t_hour = 0
            for p in piles:
                t_hour += math.ceil(p / k)

            return t_hour

        # binary search on hours (as target is in hours)
        # need to find minimum rate (k)

        l = 1 
        r = max(piles) #highest rate

        while l <= r:
            mid_rate = (l + r) // 2
            r_hour = find_hour_with_rate(mid_rate)

            if r_hour <= h:
                r = mid_rate - 1

            elif r_hour > h:
                l = mid_rate + 1

        print(l, r)
        return l