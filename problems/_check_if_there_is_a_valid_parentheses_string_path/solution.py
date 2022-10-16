class Solution:
    def hasValidPath(self, grid: List[List[str]]) -> bool:
        if grid[0][0] == ")": return False
        
        rows, cols = len(grid), len(grid[0])
        
        @cache
        def go(x, y, opened):
            if x == rows - 1 and y == cols - 1:
                return opened == 0
            
            def pos(dx, dy):
                if 0 <= dx < rows and 0 <= dy < cols:
                    if grid[dx][dy] == ")":
                        if opened >= 1:
                            return go(dx, dy, opened - 1)
                    else:
                        return go(dx, dy, opened + 1)
                        
                return False
            
            return pos(x + 1, y) or pos(x, y + 1)
        
        return go(0, 0, 1)