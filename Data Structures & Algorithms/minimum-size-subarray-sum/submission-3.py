class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        import math
        #two pointer + sliding window
        i = 0
        j = 0
        min_len = 10001

        while j < len(nums):
            print(i, j)
            if sum(nums[i : j+1]) >= target:
                min_len = min(min_len, j + 1 - i)
                i += 1
                j -= 1
            j += 1

        return 0 if min_len == 10001 else min_len