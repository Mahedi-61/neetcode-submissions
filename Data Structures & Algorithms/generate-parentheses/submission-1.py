class Solution:
    def get_candidates(self, state, n):
        if not state:
            return ["("]

        candidates = []
        close_p = state.count(")")
        open_p = state.count("(")

        if close_p > open_p:
            return []

        if n - open_p == 0:
            return [")"] 
        
        else:
            return ["(", ")"]



    def search(self, state, res, n):
        if len(state) == n*2:
            res.append("".join(state[:]))
            return 

        for candidate in self.get_candidates(state, n):
            state.append(candidate)
            
            if state.count(")") > state.count("("):
                state.pop()
                continue

            self.search(state, res, n)
            state.pop()

    def generateParenthesis(self, n: int) -> List[str]:
        state = []
        res = []
        self.search(state, res, n)
        return res