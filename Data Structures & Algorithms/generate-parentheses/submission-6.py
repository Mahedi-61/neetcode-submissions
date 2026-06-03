class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # condition p_open >= p_close
        # i == 2*n 

        def backtrack(path, p_open, p_close):
            if p_open == n and p_close == n:
                res.append("".join(path))
                return

            if p_open > n:
                return
            
            if p_close > p_open:
                return

            backtrack(path + ["("], p_open + 1, p_close)  
            backtrack(path + [")"], p_open, p_close + 1) 

        res = []
        backtrack([], 0, 0)
        return res