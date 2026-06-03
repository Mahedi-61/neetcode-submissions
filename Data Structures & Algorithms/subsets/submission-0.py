class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        sol = []

        def backtrack(idx):
            if idx == len(nums):
                res.append(sol.copy())
                return

            backtrack(idx + 1)
            sol.append(nums[idx])

            backtrack(idx + 1)
            sol.pop()

        backtrack(idx = 0)
        return res
        