class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        # merge_sort, quick_sort, insertion_sort
        # counting_sort, heap_sort, radix_sort
        def merge_sort(nums):
            if len(nums) < 2:
                return nums
            mid = len(nums) // 2
            left = merge_sort(nums[:mid])
            right = merge_sort(nums[mid:])
            return merge(left, right)

        def merge(left, right):
            combine = []
            i, j = 0, 0
            while i < len(left) and j < len(right):
                if left[i] < right[j]:
                    combine.append(left[i])
                    i += 1
                else:
                    combine.append(right[j])
                    j += 1

            combine += left[i:]
            combine += right[j:]
            return combine

        return merge_sort(nums)
            