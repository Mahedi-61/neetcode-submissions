class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        # minimal length of a subarray whose sum is greater than or equal to target. 
        # If there is no such subarray, return 0 instead.
        # A subarray is a contiguous non-empty sequence of elements
        
        #brute force solution
        # Two pointer approach
        # i = 0
        # res = []
        # while i < len(nums):
        #     t_sum = 0
        #     j = i
        #     while t_sum < target and j < len(nums):
        #         t_sum += nums[j]
        #         j += 1

        #     if t_sum >= target: res.append(j - i)
        #     i += 1

        # return min(res) if res else 0

        # O(n) solution
        # Linear
        # Two pointer but optimized

        s = 0 
        f = 0
        res = []
        t_sum = 0

        for s in range(len(nums)):
            while t_sum < target and f < len(nums):
                t_sum += nums[f]
                f += 1

            if t_sum >= target:
                t_sum -= nums[s]
                res.append(f - s)

        return min(res) if res else 0
