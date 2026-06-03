class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        
        max_sum = nums[0]
        k = len(nums)

        for j in range(k):
            temp_sum = 0
            for i in range(j, j + k):
                if nums[i % k] >= temp_sum + nums[i % k]:
                    temp_sum = nums[i % k]

                else:
                    temp_sum += nums[i % k]

                max_sum = max(max_sum, temp_sum)
        return max_sum