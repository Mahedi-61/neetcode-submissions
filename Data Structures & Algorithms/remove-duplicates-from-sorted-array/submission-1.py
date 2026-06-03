class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # nums sorted in non-decreasing order
        # return the number of unique elements,
        # first k elements of nums contain the unique elements.

        i = 1
        while i < len(nums):
            if nums[i-1] == nums[i]:
                del nums[i]
            else:
                i += 1

        return len(nums)

        