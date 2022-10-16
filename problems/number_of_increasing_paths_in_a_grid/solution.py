class Solution:
    def countPaths(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        res = 0
        M = 10 ** 9 + 7
        
        @cache
        def go(x, y):
            count = 1
            
            for dx, dy in [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]:
                if 0 <= dx < rows and 0 <= dy < cols and grid[dx][dy] > grid[x][y]:
                    count += go(dx, dy)
                    count % M
            
            return count % M
            
        
        for x in range(rows):
            for y in range(cols):
                res += go(x, y)
                res % M
        
        return res % M