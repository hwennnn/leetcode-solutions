class Solution:
    def checkMove(self, board: List[List[str]], rMove: int, cMove: int, color: str) -> bool:
        d = [-1, 0, 1]
        
        for di in d:
            for dj in d:
                x, y = rMove + di, cMove + dj
                
                if 0 <= x < 8 and 0 <= y < 8 and board[x][y] != color:
                    count = 0
                    clr = color
                    while 0 <= x < 8 and 0 <= y < 8 and board[x][y] != '.':
                        if clr != board[x][y]:
                            count += 1
                            if count == 2: return True
                            clr = board[x][y]
                        x += di
                        y += dj
                
        return False