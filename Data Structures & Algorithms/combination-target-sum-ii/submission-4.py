class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        #  The solution set must not contain duplicate combinations.
        #  candidates may be chosen at most once within a combination
        #  all unique combinations of candidates where the chosen numbers sum to target.
        candidates.sort()

        def dfs(path, start):
            total = sum(path)
            if total == target:
                res.add(tuple(path[:]))
                return

            if total > target:
                return

            for i in range(start, len(candidates)):
                if i > start and candidates[i-1] == candidates[i]:
                    continue

                path.append(candidates[i])
                dfs(path, i+1)
                path.pop()

        res = set()
        dfs([], 0)
        return [list(r) for r in res] if res else []