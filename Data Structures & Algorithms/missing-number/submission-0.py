class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        res = 0

        for i in range(len(nums) + 1):
            if i == len(nums):
                res ^= i
                break

            res = res ^ nums[i] ^ i
        return res
        