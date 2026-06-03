class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        def get_candidates(path, n):
            if path == []:
                return list(range(n))
            
            pos = len(path)
            candidates = list(range(n))
            for r, c in enumerate(path):
                if c in candidates: candidates.remove(c)

                j = pos - r
                if c + j < n and c + j in candidates: candidates.remove(c + j)
                if c - j > -1 and c - j in candidates: candidates.remove(c - j)
            return candidates

        def to_string(path):
            res = []
            for i in path:
                res.append("." * i + "Q" + "." * (n-i-1))
            return res

        def backtrack(path, sol):
            if len(path) == n:
                sol.append(to_string(path))
                return

            for can in get_candidates(path, n):
                path.append(can)
                backtrack(path, sol)
                path.pop()

        sol = []
        backtrack([], sol)
        return sol