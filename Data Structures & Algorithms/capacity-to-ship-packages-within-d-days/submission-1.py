class Solution:
    import math
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        # It is not allowed to load weight more than the maximum weight capacity of the ship.
        # must be shippe within 'days' days.
        # least weight capacity of the ship that will result in all the packages
        l = max(weights)
        r = sum(weights)
        res = r
 
        while l <= r:
            k = (l + r) // 2 #mid weight
            req_days = 1
            total_w = 0
            for w in weights:
                total_w += w
                if total_w > k:
                    req_days += 1
                    total_w = w

            if req_days <= days:  #decrease weight limit
                res = min(res, k)
                r = k - 1

            elif req_days > days: # increase weight limit
                l = k + 1

        return res

