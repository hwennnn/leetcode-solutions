class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        sx = sy = zero = 0
        
        for x in range(rows):
            for y in range(cols):
                if grid[x][y] == 0:
                    zero += 1
                elif grid[x][y] == 1:
                    sx, sy = x, y
        
        def dfs(x, y, zero):
            if grid[x][y] == 2:
                return 1 if zero == -1 else 0
            
            res = 0
            
            grid[x][y] = -1
            
            for dx, dy in [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]:
                if 0 <= dx < rows and 0 <= dy < cols and grid[dx][dy] != -1:
                    res += dfs(dx, dy, zero - 1)
            
            grid[x][y] = 0
            
            return res
        
        return dfs(sx, sy, zero)