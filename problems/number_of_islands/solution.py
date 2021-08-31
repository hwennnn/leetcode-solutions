class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows, cols = len(grid), len(grid[0])
        res = 0
        
        def dfs(x, y):
            grid[x][y] = "0"
            
            for dx, dy in [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]:
                if 0 <= dx < rows and 0 <= dy < cols and grid[dx][dy] == "1":
                    dfs(dx, dy)
        
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == "1":
                    res += 1
                    dfs(i, j)
        
        return res