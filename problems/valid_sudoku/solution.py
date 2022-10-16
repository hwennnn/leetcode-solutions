class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        usedRow = [[False] * 9 for _ in range(9)]
        usedCol = [[False] * 9 for _ in range(9)]
        usedSec = [[False] * 9 for _ in range(9)]
        
        for i in range(9):
            for j in range(9):
                if board[i][j] != '.':
                    num = ord(board[i][j]) - ord('0') - 1
                    k = i // 3 * 3 + j // 3

                    if usedRow[i][num] or usedCol[j][num] or usedSec[k][num]:
                        return False
                    
                    usedRow[i][num] = usedCol[j][num] = usedSec[k][num] = True
        
        return True