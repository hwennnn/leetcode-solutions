class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        res = 0
        
        def dfs(x, y):
            count = 1
            grid[x][y] = 0
            
            for dx, dy in [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]:
                if 0 <= dx < rows and 0 <= dy < cols and grid[dx][dy] == 1:
                    count += dfs(dx, dy)
            
            return count
        
        for x in range(rows):
            for y in range(cols):
                if grid[x][y] == 1:
                    res = max(res, dfs(x, y))
        
        return res