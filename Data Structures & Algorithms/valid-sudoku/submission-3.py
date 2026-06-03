class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        ROW = len(board)
        COL = len(board[0])

        for r in range(ROW):
            row  = []
            for c in range(COL):
                if board[r][c] != ".":
                    row.append(board[r][c])
            if len(row) != len(set(row)):
                return False

        for c in range(COL):
            col = []
            for r in range(ROW):
                if board[r][c] != ".":
                    col.append(board[r][c])

            if len(col) != len(set(col)):
                return False

        for box in range(9):
            r_start = (box // 3) * 3
            c_start = (box % 3) * 3

            grid = []
            for r in range(r_start, r_start + 3):
                for c in range(c_start, c_start + 3):
                    if board[r][c] != ".":
                        grid.append(board[r][c])

            if len(grid) != len(set(grid)):
                return False 
                
        return True

