class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        ROW = len(board)
        COL = len(board[0])

        # handling rows and columns
        for r in range(ROW):
            row = set()
            for num in board[r]:
                if num in row and num != ".":
                    return False
                row.add(num)

        for c in range(COL):
            col = set()
            for r in range(ROW):
                num = board[r][c]
                if num in col and num != ".":
                    return False
                col.add(num)

        for g in range(ROW):
            row = (g // 3) * 3
            col = (g % 3) * 3
            grid = set()
            for i in range(row, row + 3):
                for j in range(col, col + 3):
                    num =  board[i][j]
                    if num in grid and num != ".":
                        return False
                    grid.add(num)

        return True