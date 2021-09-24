class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        res = 0
        rows, cols = len(grid), len(grid[0])
        
        def dfs(x, y):
            grid[x][y] = 0
            size = 1
            
            for dx, dy in [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]:
                if 0 <= dx < rows and 0 <= dy < cols and grid[dx][dy] == 1:
                    size += dfs(dx, dy)
                    
            return size
        
        for x in range(rows):
            for y in range(cols):
                if grid[x][y] == 1:
                    res = max(res, dfs(x, y))

        return res