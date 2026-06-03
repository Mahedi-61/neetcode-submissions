class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        def backtrack(start, path):
            if start == len(nums):
                res.append(tuple(path))
                return

            #for i in range(start, len(nums)):
            i = start
            path.append(nums[i])
            backtrack(i + 1, path)
            path.pop()
            backtrack(i + 1, path)

        nums.sort()
        res = []
        backtrack(0, [])
        return list(set(res))