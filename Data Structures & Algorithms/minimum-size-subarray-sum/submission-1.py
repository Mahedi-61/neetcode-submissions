class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        # minimal length of a subarray whose sum is greater than or equal to target. 
        # If there is no such subarray, return 0 instead.
        # A subarray is a contiguous non-empty sequence of elements
        
        i = 0
        res = []
        while i < len(nums):
            t_sum = 0
            j = i
            while t_sum < target and j < len(nums):
                t_sum += nums[j]
                j += 1

            if t_sum >= target: res.append(j - i)
            i += 1

        return min(res) if res else 0