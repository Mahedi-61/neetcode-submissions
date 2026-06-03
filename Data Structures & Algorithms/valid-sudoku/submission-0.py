class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        #  checking rows
        for row in board:
            d = set()
            for i in row:
                if i in d and i != ".":
                    return False
                else:
                    d.add(i)

        # checking columns
        for j in range(len(board[0])):
            d = set()
            numbers = [row[j] for row in board if row[j] != "."]
            for j in numbers:
                if j in d:
                    return False
                else:
                    d.add(j)


        for k in range(3):
            for p in range(3):

                matrix = []
                for i in range(k*3, (k+1)*3):
                    for j in range(p*3, (p+1) * 3):
                        matrix.append(board[i][j])

                d = set()
                for m in matrix:
                    if m in d and m != ".":
                        return False
                    else:
                        d.add(m)
        return True
