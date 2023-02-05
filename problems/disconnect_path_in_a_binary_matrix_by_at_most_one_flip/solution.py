class Solution:
    def isPossibleToCutPath(self, grid: List[List[int]]) -> bool:
        rows, cols = len(grid), len(grid[0])
        
        def dfs(x, y):
            if x + 1 == rows and y + 1 == cols: return True

            if x >= rows or y >= cols or grid[x][y] == 0: return False

            grid[x][y] = 0

            return dfs(x + 1, y) or dfs(x, y + 1)
        
        if not dfs(0, 0): return True
        grid[0][0] = 1

        return not dfs(0, 0)