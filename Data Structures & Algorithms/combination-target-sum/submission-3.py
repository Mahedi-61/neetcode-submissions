class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        #backtracking (2)
        # Your task is to return a list of all unique combinations of nums
        def dfs(path, ls_idx, amount):
            if amount == 0:
                res.append(path[:])
                return

            if amount < 0:
                return

            for i in range(len(nums)):
                if not (len(ls_idx) > 0 and ls_idx[-1] > i):
                    ls_idx.append(i)
                    path.append(nums[i])

                    dfs(path, ls_idx, amount - nums[i])
                    path.pop()
                    ls_idx.pop()

        res = []
        dfs([], [], target)
        return res
            