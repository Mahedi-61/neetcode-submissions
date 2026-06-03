class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # O(n) solution
        dt_counts = set(nums)
        count = 0
        for key in dt_counts:
            curr = 1
            if key-1 not in dt_counts:
                while key + 1 in dt_counts:
                    curr += 1
                    key += 1
                    
            count = max(count, curr)

        return count

        # nums = list(set(nums)) #O(2n)
        # nums.sort() # O(n * log n)

        # count, curr = 0, 0
        # for i in range(len(nums)): # O(n)
        #     if i-1 >= 0 and nums[i] - nums[i-1] > 1:
        #         count = max(count, curr)
        #         curr = 1
        #     else:
        #         curr += 1
        
        # return max(count, curr) 