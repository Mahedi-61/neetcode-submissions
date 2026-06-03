class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        if len(nums) == 0: return False 

        values = {}
        for num in nums:
            if num in values:
                return True 
            else:
                values[num] = 1 

        return False 