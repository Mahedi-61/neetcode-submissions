class Solution:
    def rob(self, nums: List[int]) -> int:
        # bottom up (recursion)
        # bottom up (table); normal + space optimized
        def dfs(n, seen):
            if n >= len(nums):
                return 0

            if n in seen:
                return seen[n]

            seen[n] = max(nums[n] + dfs(n + 2, seen), dfs(n + 1, seen))
            return seen[n]

        seen = {}
        return dfs(0, seen)