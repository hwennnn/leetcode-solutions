class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        res = 0
        
        def go(x, y):
            if grid[x][y] == 1: return
                
            grid[x][y] = 1
            
            for dx, dy in [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]:
                if 0 <= dx < rows and 0 <= dy < cols and grid[dx][dy] != 1:
                    go(dx, dy)
        
        for x in range(rows):
            for y in range(cols):
                if x == 0 or x == rows - 1 or y == 0 or y == cols - 1:
                    go(x, y)
        
        for x in range(rows):
            for y in range(cols):
                if grid[x][y] == 0:
                    go(x, y)
                    res += 1
        
        return res