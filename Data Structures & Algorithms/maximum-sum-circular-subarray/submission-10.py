class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        global_min = nums[0]
        global_max = nums[0]
        curr_max = 0
        curr_min = 0
        total = 0

        for num in nums:
            curr_max += num
            curr_max = max(curr_max, num) 
            global_max = max(curr_max, global_max)

            curr_min += num
            curr_min = min(curr_min, num) 
            global_min = min(curr_min, global_min)
            total += num

        return max(global_max, total - global_min) if global_max > 0 else global_max 