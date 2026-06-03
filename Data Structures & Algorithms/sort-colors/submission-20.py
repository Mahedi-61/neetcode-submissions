class Solution:
    def selection_sort(self, nums):
        if len(nums) < 2: return

        for i in range(1, len(nums)):
            j = i - 1

            if nums[i] < nums[j]:
                while j >= 0 and nums[i] < nums[j]:
                    j -= 1
                j += 1
                temp = nums[i]
                nums[j+1 : i+1] = nums[j : i]
                nums[j] = temp

    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        self.selection_sort(nums)