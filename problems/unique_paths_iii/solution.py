class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        fullMask = (1 << (rows * cols)) - 1
        sx, sy = (-1, -1)
        mask = 0

        for x in range(rows):
            for y in range(cols):
                if grid[x][y] == 1:
                    sx, sy = x, y
                    mask ^= (1 << (sx * cols + sy))
                
                if grid[x][y] == -1:
                    mask ^= (1 << (x * cols + y))        

        @cache
        def go(x, y, mask):
            if grid[x][y] == 2:
                return 1 if mask == fullMask else 0
            
            res = 0
            for dx, dy in [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]:
                if 0 <= dx < rows and 0 <= dy < cols and grid[dx][dy] != -1 and mask & (1 << (dx * cols + dy)) == 0:
                    res += go(dx, dy, mask ^ (1 << (dx * cols + dy)))
            
            return res
        
        return go(sx, sy, mask)

