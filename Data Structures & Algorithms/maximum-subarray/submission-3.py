class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if (nums) == 1: return nums[0]

        row_sum = 0
        max_sum = nums[0]
        for i in range(len(nums)):
            row_sum += nums[i]
            row_sum = max(row_sum, nums[i])

            max_sum = max(max_sum, row_sum)
        return max_sum