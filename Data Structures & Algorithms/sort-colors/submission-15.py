class Solution:
    def get_pivot(self, nums, start, end):
        if len(nums) == 1: return 0 
        pivot = start
        swap = start

        for i in range(start + 1, end + 1):
            if nums[i] < nums[pivot]:
                swap += 1
                if i != swap:
                    nums[i], nums[swap] = nums[swap], nums[i]

        nums[pivot], nums[swap] = nums[swap], nums[pivot]
        pivot = swap
        return pivot 

    def quick_sort(self, nums, start, end):
        if start < end: 
            pivot = self.get_pivot(nums, start, end)
            self.quick_sort(nums, start, pivot)  
            self.quick_sort(nums, pivot+1, end) 
            
        return nums


    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # sort the array in-place such that elements of the same color are grouped together
        # order: red (0), white (1), and then blue (2).
        start = 0
        end = len(nums) - 1 
        self.quick_sort(nums, start, end)