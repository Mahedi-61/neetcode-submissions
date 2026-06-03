class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        # minimum length subarray of grater or equal to target
        i, j = 0, 0
        min_len = float("inf")
        cur_sum = 0

        while j < len(nums):
            if cur_sum < target:
                cur_sum += nums[j]
                j += 1

            while cur_sum >= target:
                min_len = min(min_len, j - i)
                cur_sum -= nums[i]
                i += 1

        return min_len if min_len != float("inf") else 0
