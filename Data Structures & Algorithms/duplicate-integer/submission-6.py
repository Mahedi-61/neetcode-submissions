class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        #return False if len(nums) == len(set(nums)) else True
        temp = set()
        for num in nums:
            if num in temp:
                return True
            temp.add(num)
        return False