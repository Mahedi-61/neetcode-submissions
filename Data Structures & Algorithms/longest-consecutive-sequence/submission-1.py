class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0: return 0 

        nums = set(nums) #has set
        max_len = 1

        for num in nums:
            count = 0
            temp = num + 1
            while (temp in nums):
                count += 1
                temp += 1

            max_len = max(max_len, count+1)

        return max_len