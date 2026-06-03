class Solution:
    def rob(self, nums: List[int]) -> int:
        memo = {}
        def dfs(idx):
            if idx >= len(nums):
                return 0

            if idx in memo:
                return memo[idx]

            memo[idx] = max(dfs(idx+2) + nums[idx], dfs(idx+1))
            return memo[idx]

        return dfs(0)