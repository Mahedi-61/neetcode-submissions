class Solution:
    def rob(self, nums: List[int]) -> int:

        def dfs(pos, seen):
            if pos >= len(nums):
                return 0 
            
            if pos in seen:
                return seen[pos]

            seen[pos] = max(nums[pos] + dfs(pos + 2, seen), dfs(pos + 1, seen))
            return seen[pos]

        res = dfs(0, seen = {})
        return res
        