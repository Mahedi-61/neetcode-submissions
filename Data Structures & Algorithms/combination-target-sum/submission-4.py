class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        #backtracking (2)
        # Your task is to return a list of all unique combinations of nums

        def dfs(path, amount, start):

            if amount == 0:
                res.append(path[:])
                return

            if amount < 0:
                return

            for i in range(start, len(nums)):
                path.append(nums[i])
                dfs(path, amount - nums[i], i)
                path.pop()

        res = []
        dfs([], target, 0)
        return res