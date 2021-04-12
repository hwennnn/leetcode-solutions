class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        res = 0
        
        def dfs(x, y):
            grid[x][y] = 0
            
            res = 0
            for dx,dy in ((x+1, y), (x - 1, y), (x, y + 1), (x, y - 1)):
                if 0 <= dx < rows and 0 <= dy < cols and grid[dx][dy] == 1:
                    res += dfs(dx, dy) + 1
            
            return res
        
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    res = max(res, dfs(i, j) + 1)
        
        return res
        