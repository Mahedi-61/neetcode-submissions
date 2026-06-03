class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # O(n) space
        dt_count = {}
        max_num, max_freq = nums[0], 1

        for num in nums:
            if num in dt_count:
                dt_count[num] += 1
                if dt_count[num] > max_freq:
                    max_freq = dt_count[num]
                    max_num = num
            else:
                dt_count[num] = 1

        return max_num
        