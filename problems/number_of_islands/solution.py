class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        def dfs(x, y):
            if not (0 <= x < rows and 0 <= y < cols) or grid[x][y] == "0": return
            
            grid[x][y] = "0"
            for dx,dy in [(x-1,y), (x+1,y), (x,y-1), (x,y+1)]:
                if 0 <= dx < rows and 0 <= dy < cols:
                    dfs(dx, dy)
                
        rows, cols = len(grid), len(grid[0])
        res = 0
        
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == "1":
                    dfs(i, j)
                    res += 1
        
        return res