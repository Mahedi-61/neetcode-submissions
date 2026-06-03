class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        #O(n) space and O(n) time 
        #T-1
        nums_set = set(nums)
        for num in range(0, len(nums)+1):
            if num not in nums_set:
                return num

        return -1