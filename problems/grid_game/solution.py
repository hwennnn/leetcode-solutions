class Solution:
    def gridGame(self, grid: List[List[int]]) -> int:
        n = len(grid[0])
        res = top = sum(grid[0])
        bottom = 0
        
        for i in range(n):
            top -= grid[0][i]
            res = min(res, max(top, bottom))
            bottom += grid[1][i]
        
        return res