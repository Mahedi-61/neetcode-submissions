class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        def get_candidates(locs):
            cans = set(list(range(n)))
            size = len(locs)
            if size == 0:
                return cans

            for i, pos in enumerate(locs):
                dr_left, dr_right = pos - (size - i), pos + (size - i)
                if dr_right < n:  cans.discard(dr_right)
                if dr_left >= 0: cans.discard(dr_left)

            for col in range(n):
                if col in set(locs):
                    cans.discard(col)
            return cans


        def display_res(ls_sols):
            res_str = []
            for sol in ls_sols:
                each_str = []
                for pos in sol:
                    each_str.append("." * pos + "Q" + "." * (n-1-pos))

                res_str.append(each_str)
            return res_str

        def backtrack(path, idx):
            if idx == n:
                res.append(path[:])
                return
            
            ls_candidates = list(get_candidates(path))
            for c in ls_candidates:
                path.append(c)
                backtrack(path, idx+1)
                path.pop()

        res = []
        backtrack([], 0)
        return display_res(res)