class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:

        def get_days_with_rate(rate):
            t_days = 0
            curr_sum = 0
            for w in weights:
                curr_sum += w
                if curr_sum > rate:
                    t_days += 1
                    curr_sum = w
            return t_days + 1

        l, r = max(weights), sum(weights)
        while l <= r:
            mid = (l + r) // 2
            print(l, r, mid)
            r_days = get_days_with_rate(mid)

            if r_days > days:
                l = mid + 1
            elif r_days <= days:
                r = mid - 1

        return l