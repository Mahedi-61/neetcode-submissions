class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        # return the maximum possible sum of a non-empty subarray
        # subarray may only include each element of the fixed buffer nums at most once

        max_sum = nums[0]
        for i in range(len(nums)):
            l = i
            temp_sum = nums[i]

            for r in range(i+1, 2 * len(nums)):
                r = r % len(nums)
                if r == l: break

                temp_sum += nums[r]
                if temp_sum < nums[r]:
                    l = r
                    temp_sum = nums[r]
                max_sum = max(temp_sum, max_sum)

        return max_sum