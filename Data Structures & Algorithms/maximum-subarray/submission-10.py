class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = nums[0]
        run_sum = max_sum

        for i in range(1, len(nums)):
            if run_sum < 0 and nums[i] > run_sum:
                run_sum = nums[i]
            else:
                run_sum += nums[i]

            max_sum = max(max_sum, run_sum)
        return max_sum
        