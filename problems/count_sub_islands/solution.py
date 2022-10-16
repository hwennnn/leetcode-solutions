class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        rows, cols = len(grid1), len(grid1[0])
        
        res = 0
        
        def dfs(x, y, path):
            grid2[x][y] = 0
            path.append((x, y))
            
            for dx, dy in ((x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)):
                if 0 <= dx < rows and 0 <= dy < cols and grid2[dx][dy] == 1:
                    dfs(dx, dy, path)
            
        
        for i in range(rows):
            for j in range(cols):
                if grid1[i][j] == grid2[i][j] == 1:
                    path = []
                    dfs(i, j, path)
                    if all(grid1[x][y] == 1 for x, y in path):
                        res += 1
        return res