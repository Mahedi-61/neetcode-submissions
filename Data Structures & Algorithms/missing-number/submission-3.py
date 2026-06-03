class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        #O(n) space and O(n) time 
        #T-1
        nums_set = set(nums)
        range_set = set(range(0, len(nums)+1))
        return list(range_set - nums_set)[0]