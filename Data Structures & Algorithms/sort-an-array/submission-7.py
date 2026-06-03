class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        # merge_sort, quick_sort, insertion_sort
        # counting_sort, heap_sort, radix_sort
        count = defaultdict(int)
        for num in nums:
            count[num] += 1
        
        max_val, min_val = max(nums), min(nums)
        res = []
        for i in range(min_val, max_val + 1):
            if count[i] > 0:
                res += count[i] * [i]
        return res 
