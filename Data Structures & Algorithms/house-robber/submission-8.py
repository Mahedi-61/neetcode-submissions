class Solution:
    def rob(self, nums: List[int]) -> int:
        
        def recur(i):
            if i == 0:
                return nums[0]
            if i == 1:
                return max(nums[0], nums[1])

            if i in memo:
                return memo[i] 

            memo[i] = max(recur(i-1), recur(i-2) + nums[i])
            return memo[i]
        
        memo = {}
        return recur(len(nums) - 1)