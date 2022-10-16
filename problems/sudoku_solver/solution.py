class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        
        def backtrack(board):
            for row in range(9):
                for col in range(9):
                    if board[row][col] == '.':
                        for x in map(str, range(1, 10)):
                            if isValid(board, row, col, x):
                                board[row][col] = x
                                
                                if backtrack(board): 
                                    return True
                                else:
                                    board[row][col] = '.'
                        
                        return False
            
            return True
        
        def isValid(board, row, col, x):
            for k in range(9):
                if board[k][col] == x: return False
                if board[row][k] == x: return False
                if board[(row // 3 * 3) + k // 3][(col // 3 * 3) + k % 3] == x: return False
            
            return True
        
        backtrack(board)
        return board
        