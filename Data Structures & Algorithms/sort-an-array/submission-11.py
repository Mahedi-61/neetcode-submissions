
import random
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        # merge_sort, quick_sort, insertion_sort
        # counting_sort, heap_sort, radix_sort
        def quick_sort(left, right):
            if left < right:
                pivot = partition(left, right)
                quick_sort(left, pivot - 1)
                quick_sort(pivot + 1, right)

        def partition(left, right):
            pivot = random.randint(left, right)
            nums[right], nums[pivot] = nums[pivot], nums[right]
            i = left - 1
            
            for j in range(left, right):
                if nums[j] < nums[right]:
                    i += 1
                    nums[i], nums[j] = nums[j], nums[i]

            nums[i + 1], nums[right] = nums[right], nums[i+1]
            return i + 1


        # def partition(left, right):
        #     pivot_index = random.randint(left, right)
        #     nums[pivot_index], nums[right] = nums[right], nums[pivot_index]
        #     pivot = nums[right]
        #     i = left - 1
        #     for j in range(left, right):
        #         if nums[j] < pivot:      # strictly less than
        #             i += 1
        #             nums[i], nums[j] = nums[j], nums[i]
        #     nums[i + 1], nums[right] = nums[right], nums[i + 1]
        #     return i + 1

        quick_sort(0, len(nums) - 1)
        return nums
            