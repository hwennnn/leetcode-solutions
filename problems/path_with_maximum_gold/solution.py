class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        
        res = 0
        
        def dfs(x, y):
            tmp = grid[x][y]
            grid[x][y] = 0
            
            total = 0
            for dx,dy in ((x+1, y), (x-1, y), (x, y-1), (x, y+1)):
                if 0 <= dx < rows and 0 <= dy < cols and grid[dx][dy] != 0:
                    total = max(total, grid[dx][dy] + dfs(dx,dy))
            
            grid[x][y] = tmp
            
            return total
                    
        
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] > 0:
                    res = max(res, grid[i][j] + dfs(i,j))
        
        return res