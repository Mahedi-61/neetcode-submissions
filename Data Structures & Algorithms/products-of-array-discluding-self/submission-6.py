class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        # O(n) operation
        prefix_mul = [1] * (len(nums) + 1)
        suffix_mul = [1] * (len(nums) + 1)

        for i in range(len(nums)):
            prefix_mul[i+1] = nums[i] * prefix_mul[i]  

        for i in range(len(nums)-1, -1, -1):
            suffix_mul[i] = nums[i] * suffix_mul[i+1]

        res = []
        for i in range(len(nums)):
            res.append(prefix_mul[i] * suffix_mul[i+1])

        return res