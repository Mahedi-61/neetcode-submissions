class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        def get_candidates(path, n):
            if path == []:
                return set(range(n))
            
            pos = len(path)
            candidates = set(range(n))
            for r, c in enumerate(path):
                candidates.discard(c)

                j = pos - r
                candidates.discard(c + j)
                candidates.discard(c - j)
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