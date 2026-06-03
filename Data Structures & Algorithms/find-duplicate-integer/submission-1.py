class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        i = 1

        while (i < n):
            if nums[i - 1] == nums[i]:
                return nums[i]
            i += 1
            
        return None