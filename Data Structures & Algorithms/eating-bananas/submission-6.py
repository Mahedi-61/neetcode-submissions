class Solution:
    # Return the minimum integer k such that you can eat all the bananas within h hours.
    # bananas-per-hour eating rate of k
    # you can not eat from another pile in the same hour.
    import math

    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        max_pile = max(piles)
        l_k = 1
        r_k = max_pile

        def get_hour(k):
            hour = 0
            for pile in piles:
                hour += int(math.ceil(pile / k))

            return hour

        res = []
        while l_k <= r_k:
            mid = (l_k + r_k) // 2
            hour = get_hour(mid) 

            if h >= hour:
                # required hour is less. so decrease the rate
                res.append(mid)
                r_k = mid - 1
                
            elif h < hour:
                # required hour is higher. so increase the rate
                l_k = mid + 1
                

        print(res)
        return min(res)