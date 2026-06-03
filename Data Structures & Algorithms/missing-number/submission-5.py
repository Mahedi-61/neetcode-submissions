class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        #O(1) space and O(n) time 
        #T-2
        n = len(nums)
        return int((n * (n+1)) / 2) - sum(nums)