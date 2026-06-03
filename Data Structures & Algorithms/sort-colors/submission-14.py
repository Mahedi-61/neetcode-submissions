class Solution:
    def get_pivot(self, nums):
        if len(nums) == 1: return 0 
        pivot = 0
        swap = 0
        for i in range(1, len(nums)):
            if nums[i] < nums[pivot]:
                swap += 1
                if i != swap:
                    nums[i], nums[swap] = nums[swap], nums[i]

        nums[pivot], nums[swap] = nums[swap], nums[pivot]
        pivot = swap
        return pivot 

    def quick_sort(self, nums):
        if len(nums) < 2: return nums

        pivot = self.get_pivot(nums)
        # left = self.quick_sort(nums[ : pivot])
        # right = self.quick_sort(nums[ pivot + 1 : ])
        return self.quick_sort(nums[ : pivot]) + [nums[pivot]] +  self.quick_sort(nums[ pivot + 1 : ]) 

    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # sort the array in-place such that elements of the same color are grouped together
        # order: red (0), white (1), and then blue (2).

        nums[:] = self.quick_sort(nums)