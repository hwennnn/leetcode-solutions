class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        mp = collections.defaultdict(int)
        colorIndex = 2
        
        def dfs(x, y, color):
            size = 1
            grid[x][y] = color
            
            for dx, dy in ((x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)):
                if 0 <= dx < rows and 0 <= dy < cols and grid[dx][dy] == 1:
                    size += dfs(dx, dy, color)
            
            return size
        
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    size = dfs(i, j, colorIndex)
                    mp[colorIndex] = size
                    colorIndex += 1
                    
        res = mp[2]
        for x in range(rows):
            for y in range(cols):
                if grid[x][y] == 0:
                    size = 1
                    sset = set()
                    
                    for dx, dy in ((x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)):
                        if 0 <= dx < rows and 0 <= dy < cols and grid[dx][dy] not in sset:
                            size += mp[grid[dx][dy]]
                            sset.add(grid[dx][dy])
                    
                    res = max(res, size)
        
        return res