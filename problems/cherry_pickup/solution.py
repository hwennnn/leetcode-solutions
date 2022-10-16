class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        n = len(grid)
        directions = [(1, 0), (0, 1)]
        
        @cache
        def go(r1, c1, r2, c2):
            if r1 == r2 == c1 == c2 == n - 1: return 0
            
            res = float('-inf')
            
            for dx1, dy1 in directions:
                R1, C1 = r1 + dx1, c1 + dy1
                if not (0 <= R1 < n and 0 <= C1 < n and grid[R1][C1] != -1): continue
                for dx2, dy2 in directions:
                    R2, C2 = r2 + dx2, c2 + dy2
                    
                    if 0 <= R2 < n and 0 <= C2 < n and grid[R2][C2] != -1:
                        cherries = grid[R1][C1] + (grid[R2][C2] * int((R1, C1) != (R2, C2)))
                        res = max(res, go(R1, C1, R2, C2) + cherries)
            
            return res
        
        return max(0, go(0, 0, 0, 0) + grid[0][0])