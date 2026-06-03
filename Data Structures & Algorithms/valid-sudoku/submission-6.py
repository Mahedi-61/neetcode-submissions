class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # single pass
        ROW = len(board)
        COL = len(board[0])
        dt_rows = defaultdict(set)
        dt_cols = defaultdict(set)
        dt_grids = defaultdict(set)

        for r in range(ROW):
            for c in range(COL):
                if board[r][c] == ".":
                    continue
                
                num = board[r][c]
                if (num in dt_rows[r] or 
                    num in dt_cols[c] or
                    num in dt_grids[(r//3, c//3)]):
                    return False

                dt_rows[r].add(board[r][c])
                dt_cols[c].add(board[r][c])
                dt_grids[(r//3, c//3)].add(board[r][c])

        return True