class Solution:
    def solve(self, board: List[List[str]]) -> None:
        ROW = len(board)
        COL = len(board[0])

        # do dfs() from that 0's convert them to 1's
        def dfs(i, j):
            if (i < 0 or i >= ROW or j < 0 or j >= COL or 
                board[i][j] == "1" or board[i][j] == "X"):
                return 

            board[i][j] = "1"
            dfs(i+1, j)
            dfs(i-1, j)
            dfs(i, j+1)
            dfs(i, j-1)

        # scan first row, col | last row, col for 0's
        for r in [0, ROW-1]:
            for c in range(COL):
                if board[r][c] == "O":
                    dfs(r, c)

        for c in [0, COL-1]:
            for r in range(ROW):
                if board[r][c] == "O":
                    dfs(r, c)

        # finally convert all 0's -> X and 1's -> 0 (inplace)
        for r in range(ROW):
            for c in range(COL):
                if board[r][c] == "O":
                    board[r][c] = "X"
                    
                elif board[r][c] == "1":
                    board[r][c] = "O"