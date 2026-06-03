class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        #if len(nums) == 1: return nums[0]
        # max_sum = nums[0] 

        # for i in range(len(nums)): #O(n**2)
        #     row_sum = 0

        #     for j in range(i, len(nums)):
        #         row_sum += nums[j]
        #         max_sum = max(max_sum, row_sum)

        # return max_sum
        if len(nums) == 1: return nums[0]
        # row_sum = 0
        # max_sum = nums[0]

        # for i in range(len(nums)): # O(1)
        #     row_sum += nums[i]
        #     row_sum = max(row_sum, nums[i])
        #     max_sum = max(max_sum, row_sum)

        # return max_sum

        dp = [*nums]
        for i in range(1, len(nums)):
            dp[i] = max(nums[i], nums[i] + dp[i - 1])
        
        return max(dp)