class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        #kdanes algorithm

        max_sum = nums[0]
        min_sum = nums[0]

        curr_max_sum = 0
        curr_min_sum = 0
        total = 0

        for num in nums:
            curr_max_sum = max(curr_max_sum + num, num)
            curr_min_sum = min(curr_min_sum + num, num)

            total += num
            max_sum = max(max_sum, curr_max_sum)
            min_sum = min(min_sum, curr_min_sum)

        return max(max_sum, total - min_sum) if max_sum > 0 else max_sum