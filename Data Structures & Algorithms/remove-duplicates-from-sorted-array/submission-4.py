class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) < 2: return len(nums)
        i = 1

        while i < len(nums):
            if nums[i] == nums[i-1]: #unique elements
                del nums[i]
            else:
                i += 1

        return i