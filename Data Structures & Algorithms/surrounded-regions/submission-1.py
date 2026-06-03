class Solution:
    def solve(self, board: List[List[str]]) -> None:
        ROW = len(board)
        COL = len(board[0])
        visit_zeros = set()

        def dfs(i, j):
            if board[i][j] == "T":
                surr[0] = False
                return
            if board[i][j] == "X":
                return
            if (i, j) in visit:
                return

            visit.add((i, j))
            dfs(i, j+1)
            dfs(i, j-1)
            dfs(i+1, j)
            dfs(i-1, j)

        # mark border 0's to T
        for r in [0, ROW-1]:
            for c in range(COL):
                if board[r][c] == "O":
                    board[r][c] = "T"

        for c in [0, COL-1]:
            for r in range(ROW):
                if board[r][c] == "O":
                    board[r][c] = "T"

        # main logic
        for r in range(1, ROW-1):
            for c in range(1, COL-1):
                if board[r][c] == "O" and board[r][c] not in visit_zeros:
                    visit = set()
                    surr = [True]
                    dfs(r, c)

                    if surr == [True]:
                        for i, j in visit:
                            board[i][j] = "X"
                    else:
                        visit_zeros.update(visit)

        # mark border T's to O's again
        for r in [0, ROW-1]:
            for c in range(COL):
                if board[r][c] == "T":
                    board[r][c] = "O"

        for c in [0, COL-1]:
            for r in range(ROW):
                if board[r][c] == "T":
                    board[r][c] = "O"
