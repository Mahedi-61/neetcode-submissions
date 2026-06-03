class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if (nums) == 1: return nums[0]
        max_sum = nums[0] 

        for i in range(len(nums)): #O(n**2)
            row_sum = 0

            for j in range(i, len(nums)):
                row_sum += nums[j]
                max_sum = max(max_sum, row_sum)

        return max_sum