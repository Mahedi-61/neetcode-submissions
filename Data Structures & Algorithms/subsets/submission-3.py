class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []

        def dfs(i, status):
            if i == len(nums):
                res.append(status)
                return

            dfs(i+1, status + [nums[i]])
            dfs(i+1, status)

        dfs(0, [])
        return res