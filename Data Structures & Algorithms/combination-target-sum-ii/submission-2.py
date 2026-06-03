class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        #all unique combinations of candidates
        # may be chosen at most once within a combination.
        #combination can be in any order.

        res = set()
        def backtrack(path, tg, start):
            if tg == 0:
                array = tuple(sorted(path[:]))
                if array not in res:
                    res.add(array)
                return

            for i in range(start, len(candidates)):
                if tg - candidates[i] >= 0:
                    path.append(candidates[i])
                    backtrack(path, tg - candidates[i], i+1)
                    path.pop()

        backtrack([], target, 0)
        return [list(r) for r in res]