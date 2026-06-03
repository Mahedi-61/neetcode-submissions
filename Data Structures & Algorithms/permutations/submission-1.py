class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        res = []
        def backtrack(path, start):
            if len(path) == len(nums):
                res.append(path.copy())
                return

            for i in range(len(nums)):
                if nums[i] not in path:
                    path.append(nums[i])
                    backtrack(path, i+1)
                    path.pop()

        backtrack([], 0)
        return [list(r) for r in res]