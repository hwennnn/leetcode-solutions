class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        
        # Any live cell with fewer than two live neighbors dies as if caused by under-population.
        # Any live cell with two or three live neighbors lives on to the next generation.
        # Any live cell with more than three live neighbors dies, as if by over-population.
        # Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.

        rows, cols = len(board), len(board[0])
        
        def findNeighbours(r,c):
            count = 0
            nei = [(x,y) for x in (0,-1,1) for y in (0,-1,1) if x != 0 or y != 0]

            for x,y in nei:
                dx, dy = r + x, c + y
                if 0 <= dx < rows and 0 <= dy < cols and board[dx][dy] % 2: count += 1

            return count
            
        for r in range(rows):
            for c in range(cols):
                count = findNeighbours(r,c)
                
                if board[r][c] == 1:
                    if not (2 <= count <= 3): board[r][c] = 3
                else:
                    if count == 3: board[r][c] = 2
        
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == 2: board[r][c] = 1
                
                elif board[r][c] == 3: board[r][c] = 0
    
                            
                            
        
        