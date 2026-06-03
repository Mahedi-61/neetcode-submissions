class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = list(set(nums)) #O(2n)
        nums.sort() # O(n * log n)

        if len(nums) < 2:
            return len(nums)

        count = 0
        curr = 1
        print(nums)
        for i in range(1, len(nums)): # O(n)
            if nums[i] - nums[i-1] > 1:
                count = max(count, curr)
                curr = 1

            else:
                curr += 1
        
        print(count, curr)
        return max(count, curr) 