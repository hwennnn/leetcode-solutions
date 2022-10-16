class Solution:
    def countPyramids(self, grid: List[List[int]]) -> int:
        reversedGrid = [row[:] for row in grid][::-1]
        rows, cols = len(grid), len(grid[0])
        
        def count(grid):
            res = 0
            
            for x in range(1, rows):
                for y in range(1, cols - 1):
                    if grid[x][y] and grid[x - 1][y]:
                        grid[x][y] = 1 + min(grid[x - 1][y - 1], grid[x - 1][y + 1])
                        res += grid[x][y] - 1
            
            return res
        
        return count(grid) + count(reversedGrid)