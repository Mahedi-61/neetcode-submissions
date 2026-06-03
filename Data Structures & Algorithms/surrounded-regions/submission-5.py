class Solution:
    def solve(self, board: List[List[str]]) -> None:
        ROW = len(board)
        COL = len(board[0])

        def dfs(i, j):
            if (i < 0 or i >= ROW or j < 0 or j >= COL 
                or (i, j) in visit or board[i][j] == "X"):
                return

            if board[i][j] == "O":
                board[i][j] = "#"
            visit.add((i, j))

            dfs(i+1, j)
            dfs(i-1, j)
            dfs(i, j+1)
            dfs(i, j-1)

        visit = set()
        for r in [0, ROW-1]:
            for c in range(COL):
                if board[r][c] == "O" and (r, c) not in visit:
                    dfs(r, c)

        for c in [0, COL-1]:
            for r in range(ROW):
                if board[r][c] == "O" and (r, c) not in visit:
                    dfs(r, c)

        # final work
        for r in range(ROW):
            for c in range(COL):
                if board[r][c] == "O":
                    board[r][c] = "X"
                elif board[r][c] == "#":
                    board[r][c] = "O"


