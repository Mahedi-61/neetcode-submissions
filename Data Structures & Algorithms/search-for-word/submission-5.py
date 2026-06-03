class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        if not board or not board[0]:
            return False

        ROW = len(board)
        COL = len(board[0])

        def dfs(i, j, k, path):
            if (i < 0 or i >= ROW or j < 0 or j >= COL or 
                (i, j) in path or board[i][j] != word[k]):
                return False

            path.add((i, j))
            if k == len(word) - 1:
                return True
            
            status = (dfs(i+1, j, k+1, path) or 
            dfs(i-1, j, k+1, path) or 
            dfs(i, j+1, k+1, path) or
            dfs(i, j-1, k+1, path))

            if not status: path.discard((i, j))
            return status

        
        for r in range(ROW):
            for c in range(COL):
                if board[r][c] == word[0]:
                    if dfs(r, c, 0, set()):
                        return True

        return False

