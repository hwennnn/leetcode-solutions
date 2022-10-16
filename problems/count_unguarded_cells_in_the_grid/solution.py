class Solution:
    def countUnguarded(self, rows: int, cols: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        grid = [[1] * cols for _ in range(rows)]
        
        for x, y in walls:
            grid[x][y] = -1
            
        def goLeft(x, y):
            dy = y - 1
            while dy >= 0 and grid[x][dy] != 2 and grid[x][dy] != -1:
                grid[x][dy] = 2
                dy -= 1
        
        def goRight(x, y):
            dy = y + 1
            while dy < cols and grid[x][dy] != 3 and grid[x][dy] != -1:
                grid[x][dy] = 3
                dy += 1
                
        def goTop(x, y):
            dx = x - 1
            while dx >= 0 and grid[dx][y] != 4 and grid[dx][y] != -1:
                grid[dx][y] = 4
                dx -= 1
                
        def goBottom(x, y):
            dx = x + 1
            while dx < rows and grid[dx][y] != 5 and grid[dx][y] != -1:
                grid[dx][y] = 5
                dx += 1
    
        guards.sort(key = lambda x : (-x[1], x[0]))

        for x, y in guards:
            goLeft(x, y)

        guards.sort(key = lambda x : (x[1], x[0]))

        for x, y in guards:
            goRight(x, y)
        
        guards.sort(key = lambda x : (-x[0], x[1]))
        for x, y in guards:
            goTop(x, y)

        guards.sort(key = lambda x : (x[0], x[1]))
        for x, y in guards:
            goBottom(x, y)

        for x, y in guards:
            grid[x][y] = -1
        
        res = 0
        
        for x in range(rows):
            for y in range(cols):
                if grid[x][y] == 1:
                    res += 1
        
        return res