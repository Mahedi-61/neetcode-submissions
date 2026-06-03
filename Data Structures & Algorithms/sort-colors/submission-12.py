class Solution:
    def sortColors(self, nums: List[int]) -> None:
        if len(nums) < 2: 
            return 

        i = 0
        j = 0
        while i < len(nums):
            if (nums[i] == 0):
                nums[j], nums[i] = nums[i], nums[j]
                j += 1
            i += 1

        i = len(nums) - 1
        k = len(nums) - 1
        while i > 0:
            if nums[i] == 2:
                nums[i], nums[k] = nums[k], nums[i]
                k -= 1
            i -= 1