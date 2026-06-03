class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        n = len(nums)
        total = 0
        i = 0 
        while i < n:

            if nums[abs(nums[i]) - 1] > 0:
                nums[abs(nums[i]) - 1] *= -1 
                i += 1 
            else:
                return abs(nums[i])

        return None