class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if (nums) == 1: return nums[0]
        max_sum = nums[0] 

        for i in range(len(nums)):
            row_sum = nums[i]
            max_sum = max(max_sum, row_sum)

            for j in range(i + 1, len(nums)):
                row_sum += nums[j]
                max_sum = max(max_sum, row_sum)

        return max_sum