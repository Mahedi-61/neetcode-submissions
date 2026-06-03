class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # time: O(n) & space: O(n)
        n = len(nums)
        prefix_mul = [0] * n 
        postfix_mul = [0] * n
        result = []

        prefix_mul[0] = postfix_mul[n-1] = 1 
        for i in range(1, n):
            prefix_mul[i] = prefix_mul[i - 1] * nums[i - 1]

        for i in range(n-2, -1, -1):
            postfix_mul[i] = postfix_mul[i + 1] * nums[i + 1]

        for i in range(n):
            result.append(postfix_mul[i] * prefix_mul[i])

        return result