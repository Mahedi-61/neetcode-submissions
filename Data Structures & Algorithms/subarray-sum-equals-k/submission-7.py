class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        #O(n*2) solution
        prefix_sum = [0] * (len(nums) + 1)
        for i, num in enumerate(nums):
            prefix_sum[i+1] = prefix_sum[i] + nums[i]

        prefix_set = set(prefix_sum[1: ])

        i = 0
        count = 0
        for i in range(len(nums)):
            total = 0
            if prefix_sum[i] + k in prefix_set:
                for j in range(i, len(nums)):
                    total += nums[j]
                    if total == k:
                        count += 1

        return count

