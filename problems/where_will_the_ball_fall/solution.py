class Solution:
    def findBall(self, grid: List[List[int]]) -> List[int]:
        rows, cols = len(grid), len(grid[0])
        
        def go(x, y):
            if x == rows: return y

            if grid[x][y] == 1:
                if y == cols - 1 or grid[x][y + 1] == -1:
                    return -1
                
                return go(x + 1, y + 1)
            else:
                if y == 0 or grid[x][y - 1] == 1:
                    return -1
                
                return go(x + 1, y - 1)
            
        return [go(0, y) for y in range(cols)]