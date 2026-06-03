class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1: return nums[0]
        
        def do_rob(data):
            prev_max, curr_max = 0, 0

            for num in data:
                if num + prev_max > curr_max:
                    temp = num + prev_max
                else:
                    temp = curr_max

                prev_max = curr_max
                curr_max = temp

            return curr_max

        return max(do_rob(nums[:-1]), do_rob(nums[1:]))