class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROW = len(board)
        COL = len(board[0])
        BDS = ROW * COL
        if len(word) > BDS: return False 
        
        def dfs(i, j, idx, visit):
            if board[i][j] != word[idx]:
                return False

            if idx == len(word)-1:
                return True

            visit.add((i, j))
            ans = False
            for di, dj in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
                n_i, n_j = i + di, j + dj

                if (n_i < 0 or n_i >= ROW or n_j < 0 or n_j >= COL):
                    continue

                if (n_i, n_j) in visit:
                    continue

                ans = ans or dfs(n_i, n_j, idx+1, visit)
                if ans == True:
                    return True
                else:
                    if visit: visit.discard((n_i, n_j))
                    dfs(i, j, idx-1, visit)

        for r in range(ROW):
            for c in range(COL):
                if board[r][c] == word[0]:
                    if dfs(r, c, 0, set()):
                        return True

        return False