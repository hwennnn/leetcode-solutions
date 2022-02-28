class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows, cols = len(grid), len(grid[0])
        
        def dfs(x, y):
            grid[x][y] = "0"
            
            for dx, dy in [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]:
                if 0 <= dx < rows and 0 <= dy < cols and grid[dx][dy] == "1":
                    dfs(dx, dy)
        
        res = 0
        for x in range(rows):
            for y in range(cols):
                if grid[x][y] == "1":
                    dfs(x, y)
                    res += 1
        
        return res