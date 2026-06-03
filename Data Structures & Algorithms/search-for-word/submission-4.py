class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROW = len(board)
        COL = len(board[0])
        if len(word) > ROW * COL: return False 
        
        def dfs(i, j, idx, visit):
            if board[i][j] != word[idx]:
                return False

            if idx == len(word)-1:
                return True

            visit.add((i, j))
            ans = False
            for di, dj in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
                n_i, n_j = i + di, j + dj

                if not (n_i < 0 or n_i >= ROW or n_j < 0 or n_j >= COL or (n_i, n_j) in visit):
                    if dfs(n_i, n_j, idx+1, visit):
                        return True

            visit.remove((i, j))

        for r in range(ROW):
            for c in range(COL):
                if board[r][c] == word[0]:
                    if dfs(r, c, 0, set()):
                        return True

        return False