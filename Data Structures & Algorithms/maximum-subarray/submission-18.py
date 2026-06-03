class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # start from index 0 and go through end
        # check & save max_array
        # any num which makes it 0 or - you can start from begining
        # no prefix_sum

        i = 0
        max_array = nums[0]
        temp = 0

        while i < len(nums):
            max_array = max(max_array, nums[i])

            temp += nums[i]
            if temp > 0:
                max_array = max(max_array, temp)
            else:
                temp = 0

            i += 1

        return max_array
