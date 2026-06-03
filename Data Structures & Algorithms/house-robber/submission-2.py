class Solution:
    def rob(self, nums: List[int]) -> int:
        prev_max, curr_max = 0, 0

        for num in nums:
            temp = max(prev_max + num, curr_max)
            prev_max = curr_max
            curr_max = temp

        return curr_max