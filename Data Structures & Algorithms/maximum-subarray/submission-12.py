class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        prefix_sum = 0
        max_sum = nums[0]

        for num in nums:
            prefix_sum = max(prefix_sum + num, num)
            max_sum = max(prefix_sum, max_sum)

        return max_sum