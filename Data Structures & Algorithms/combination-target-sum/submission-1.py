class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def backtrack(path, target):
            if target == 0:
                res.append(path.copy())
                return

            for choice in nums:
                if target - choice < 0:
                    continue

                path.append(choice)
                backtrack(path, target-choice)
                path.pop()

        backtrack([], target)
        final_res = []
        for r in res:
            d = defaultdict(int)
            for val in r: d[val] += 1
            if d not in final_res:
                final_res.append(d)

        ans = []
        for fd in final_res:
            temp = []
            for key in fd:
                temp += [key]*fd[key] 

            ans.append(temp)
        return ans