class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        # bigger sum -> lower k
        l, r = max(nums), sum(nums)

        def calculate_k(sub_sum):
            total_k = 0
            curr_sum = 0

            for num in nums:
                curr_sum += num

                if curr_sum > sub_sum:
                    total_k += 1
                    curr_sum = num

            return total_k + 1
        
        while l <= r:
            mid_sub_sum = (l + r) // 2
            r_k = calculate_k(mid_sub_sum)

            if r_k > k:
                l = mid_sub_sum + 1

            elif r_k <= k:
                r = mid_sub_sum - 1

        return l  