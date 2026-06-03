class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        # merge_sort, quick_sort, insertion_sort
        # counting_sort, heap_sort, radix_sort
        max_val, min_val = max(nums), min(nums)
        count = [0] * (max_val - min_val + 1)

        for num in nums:
            idx = num - min_val
            count[idx] += 1

        res = []
        for idx, freq in enumerate(count):
            if count[idx] > 0:
                res.extend([idx + min_val] * freq)
        return res 