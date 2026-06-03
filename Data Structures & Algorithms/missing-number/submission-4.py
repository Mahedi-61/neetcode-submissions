class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        #O(1) space and O(n) time 
        #T-2
        res = 0
        for i in range(0, len(nums)+1):
            res ^= i

        for num in nums:
            res ^= num
        return res