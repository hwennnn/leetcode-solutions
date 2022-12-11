class Solution:
    def deleteGreatestValue(self, grid: List[List[int]]) -> int:
        for row in grid:
            row.sort()
        
        res = 0
        for col in zip(*grid):
            res += max(col)
        
        return res