class Solution:
    def findDuplicate(self, nums: List[int]) -> int:

        # O(n*log_n) solution (O(1) space)
        # brute force 
        # nums.sort()
        # for i in range(1, len(nums)):
        #     if nums[i-1] == nums[i]:
        #         return nums[i]

        # O(1) solution O(n) space
        hash_set = set()
        for num in nums:
            if num not in hash_set:
                hash_set.add(num)
            else:
                return num