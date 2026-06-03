class Solution:
    def get_pivot(self, nums, start, end):
        pivot = start
        swap = start
        for i in range(start+1, end+1):
            if nums[i] < nums[pivot]:
                swap += 1
                if i != swap:
                    nums[swap], nums[i] = nums[i], nums[swap]

        nums[swap], nums[pivot] = nums[pivot], nums[swap]
        pivot = swap 
        return pivot 

    def quick_sort(self, nums, left, right):
        if left < right:
            p_index = self.get_pivot(nums, left, right)
            self.quick_sort(nums, left, p_index-1)
            self.quick_sort(nums, p_index+1, right)


    def sortColors(self, nums: List[int]) -> None:
        self.quick_sort(nums, 0, len(nums)-1)