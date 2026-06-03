class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        ROW = len(board)
        COL = len(board[0])

        # handling rows and columns
        for r in range(ROW):
            row = []
            for num in board[r]:
                if num != ".":
                    row.append(num)
            if len(row) != len(set(row)): 
                return False

        for c in range(COL):
            col = []
            for r in range(ROW):
                if board[r][c] != ".":
                    col.append(board[r][c])
            if len(col) != len(set(col)):
                return False

        for g in range(ROW):
            row = (g // 3) * 3
            col = (g % 3) * 3
            grid = []
            for i in range(row, row + 3):
                for j in range(col, col + 3):
                    if board[i][j] != ".":
                        grid.append(board[i][j])

            if len(grid) != len(set(grid)):
                return False

        return True