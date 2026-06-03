class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = 0
        right = 0
        min_len = float("inf")
        curr_sum = 0

        while right < len(nums):
            curr_sum += nums[right]
            while curr_sum >= target:
                min_len = min(min_len, right + 1 - left)
                curr_sum -= nums[left]
                left += 1

            right += 1 

        return 0 if min_len == float("inf") else min_len