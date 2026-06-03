class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = list(set(nums)) #O(2n)
        nums.sort() # O(n * log n)

        count = 0
        curr = 0
        for i in range(len(nums)): # O(n)
            if i-1 >= 0 and nums[i] - nums[i-1] > 1:
                count = max(count, curr)
                curr = 1

            else:
                curr += 1
        
        return max(count, curr) 