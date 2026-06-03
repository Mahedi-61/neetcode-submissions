class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        nums.sort()

        size = len(nums) // 3
        result = []
        i = 0
        while i < len(nums):
            j = i + 1

            while j < len(nums) and nums[i] == nums[j]:
                j += 1

            if (j - i) > size:
                result.append(nums[j - 1])

            i = j
        return result