class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # O(n) time and O(1) space without division operator
        res = [1] * len(nums)

        prefix = 1
        for i in range(len(nums)):
            res[i] = res[i] * prefix
            prefix *= nums[i] 

        postfix = 1
        for i in range(len(nums)-1, -1, -1):
            res[i] = res[i] * postfix
            postfix *= nums[i]

        return res
        