class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        # can be solved with iteration + recursion 

        def backtrack(start, path):
            p = path[:]
            if len(p) == 0:
                res[0] += 0
            elif len(p) == 1:
                res[0] += p[0]
            else:
                temp = 0
                for j in path:
                    temp ^= j
                res[0] += temp

            for i in range(start, len(nums)):
                path.append(nums[i])
                backtrack(i + 1, path)
                path.pop()

        res = [0]
        backtrack(0, [])
        return res[0]
        # dfs