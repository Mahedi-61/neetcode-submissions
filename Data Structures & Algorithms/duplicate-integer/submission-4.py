class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        if len(nums) == 0: return False 

        #seen = set() # hash set
        seen = dict() # has table
        for num in nums:
            if num in seen:
                return True 
            else:
                #seen.add(num) 
                seen[num] = 1 
        return False 