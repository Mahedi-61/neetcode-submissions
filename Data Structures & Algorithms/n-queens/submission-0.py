class Solution:
    def available_pos(self, state, n):
        if not state:
            return range(n)

        # all available position before pruning
        all_pos = set(range(n))

        # do the pruning
        for row, col in enumerate(state):
            # discarding columns
            all_pos.discard(col)

            # discarding diagonals
            dist = len(state) - row
            all_pos.discard(col - dist)
            all_pos.discard(col + dist)

        return all_pos

    def to_string(self, state, n):
        string = []
        for i in state:
            string.append("." * i + "Q" + "." * (n - i - 1))

        return string 


    def search(self, state, res, n):
        if len(state) == n:
            res.append(self.to_string(state, n))
            return 

        for pos in self.available_pos(state, n):
            state.append(pos)
            self.search(state, res, n)
            state.pop()


    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []
        state = []
        self.search(state, res, n)
        return res