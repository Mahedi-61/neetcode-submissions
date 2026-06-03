class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        if len(nums) == 1: return nums[0]

        count = {}
        max_len = 0
        maj_el = nums[0]

        for num in nums:
            if num in count:
                count[num] += 1

            else:
                count[num] = 1

            if max_len < count[num]:
                max_len = count[num]
                maj_el = num 

        return maj_el