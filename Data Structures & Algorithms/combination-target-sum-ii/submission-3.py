class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        #all unique combinations of candidates
        # may be chosen at most once within a combination.
        #combination can be in any order.

        res = []
        candidates.sort()
        def backtrack(path, tg, start):
            if tg == 0:
                res.append(path[:])
                return

            for i in range(start, len(candidates)):
                if i > start and candidates[i] == candidates[i-1]:
                    continue
                if tg - candidates[i] >= 0:
                    path.append(candidates[i])
                    backtrack(path, tg - candidates[i], i+1)
                    path.pop()

        backtrack([], target, 0)
        return res