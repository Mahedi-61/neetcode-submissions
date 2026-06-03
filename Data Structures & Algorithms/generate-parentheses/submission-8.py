class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        def backtrack(path, p_open, p_close):
            if p_open == p_close == n:
                res.append("".join(path))
                return

            if p_open < n:
                path.append("(")
                backtrack(path, p_open+1, p_close)
                path.pop()

            if p_close < p_open:
                path.append(")")
                backtrack(path, p_open, p_close + 1)
                path.pop()

        res = []
        backtrack([], 0, 0)
        return res