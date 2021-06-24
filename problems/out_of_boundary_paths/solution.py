class Solution:
    def findPaths(self, rows: int, cols: int, maxMove: int, startRow: int, startColumn: int) -> int:
        
        @cache
        def go(x, y, moves):
            if not (0 <= x < rows and 0 <= y < cols): return 1
            
            if moves == maxMove: return 0
            
            res = 0
            
            for dx, dy in ((x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)):
                res += go(dx, dy, moves + 1)
            
            return res
        
        return go(startRow, startColumn, 0) % (10 ** 9 + 7)