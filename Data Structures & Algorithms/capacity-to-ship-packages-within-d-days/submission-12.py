import math 
class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        if len(weights) <= days:
            return max(weights)

        def check_capacity(cap):
            req_days = 0
            curr_sum = 0

            for w in weights:
                curr_sum += w
                if curr_sum > cap:
                    req_days += 1
                    curr_sum = w

            return req_days + 1 <= days

        l = max(weights)
        r = sum(weights)

        while l < r:
            mid = (l + r) // 2
            if check_capacity(mid): #yes can ship. Need smaller weights
                r = mid

            else: # No heavier weights
                l = mid + 1
        return r