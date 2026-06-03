class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        #write the O(n**2) solution
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] == nums[j]:
                    return True
        return False