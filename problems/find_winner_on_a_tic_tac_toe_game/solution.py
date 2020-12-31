class Solution:
    def tictactoe(self, moves: List[List[int]]) -> str:
        grid = [[""]*3 for _ in range(3)]
        
        player = 0
        for r,c in moves:
            grid[r][c] = "X" if player % 2 == 0 else "O"
            player += 1
            
        for r in range(3):
            if all(b == "X" for b in grid[r]): return "A"
            elif all(b == "O" for b in grid[r]): return "B"
            
        for c in range(3):
            if all(grid[i][j] == "X" for i in range(3) for j in range(3) if j == c): return "A"
            elif all(grid[i][j] == "O" for i in range(3) for j in range(3) if j == c): return "B"
                     
        if all(grid[r][c] == "X" for r in range(3) for c in range(3) if r == c): return "A"
        if all(grid[r][c] == "O" for r in range(3) for c in range(3) if r == c): return "B"
        
        if all(grid[r][c] == "X" for r in range(2,-1,-1) for c in range(2,-1,-1) if r + c == 2): return "A"
        if all(grid[r][c] == "O" for r in range(2,-1,-1) for c in range(2,-1,-1) if r + c == 2): return "B"
        
        
        return "Draw" if player == 9 else "Pending"