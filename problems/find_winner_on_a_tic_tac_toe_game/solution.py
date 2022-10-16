class Solution:
    def tictactoe(self, moves: List[List[int]]) -> str:
        n = 3
        rows = [0] * n
        cols = [0] * n
        diag1 = diag2 = 0
        currPlayer = 1
        
        for x, y in moves:
            rows[x] += currPlayer
            cols[y] += currPlayer
            diag1 = diag1 + currPlayer if x == y else diag1
            diag2 = diag2 + currPlayer if x + y == n - 1 else diag2
            
            if abs(rows[x]) == n or abs(cols[y]) == n or abs(diag1) == n or abs(diag2) == n:
                return "A" if currPlayer == 1 else "B"
            
            currPlayer *= -1
        
        return "Draw" if len(moves) == n * n else "Pending"