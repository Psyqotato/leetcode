class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(0,9):
            line = ['1','2','3','4','5','6','7','8','9']
            row = ['1','2','3','4','5','6','7','8','9']
            if i % 3 == 0:
                k = 0
                while k <= 2:
                    box = ['1','2','3','4','5','6','7','8','9']
                    for x in range(i,i+3):
                        for y in range(k*3,k*3+3):
                            if board[x][y] != '.' and board[x][y] in box:
                                box.remove(board[x][y])
                            elif board[x][y] != '.' and board[x][y] not in box:return False
                            else:pass
                    k += 1
            for j in range(0,9):
                if board[i][j] != '.' and board[i][j] in line:
                    line.remove(board[i][j])
                elif board[i][j] != '.' and board[i][j] not in line:return False
                else:pass
                if board[j][i] != '.' and board[j][i] in row:
                    row.remove(board[j][i])
                elif board[j][i] != '.' and board[j][i] not in row:return False
                else:pass
        return True