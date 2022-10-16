class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        queue = deque()
        
        def dfs(x, y):
            grid[x][y] = -1
            queue.append((x, y))
            
            for dx, dy in [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]:
                if 0 <= dx < rows and 0 <= dy < cols and grid[dx][dy] == 1:
                    dfs(dx, dy)
        
        flag = False
        for x in range(rows):
            for y in range(cols):
                if grid[x][y] == 1:
                    flag = True
                    dfs(x, y)
                    break
            
            if flag: break
        
        steps = 0
        while queue:
            n = len(queue)
            
            for _ in range(n):
                x, y = queue.popleft()
                
                for dx, dy in [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]:
                    if 0 <= dx < rows and 0 <= dy < cols and grid[dx][dy] != -1:
                        if grid[dx][dy] == 1: return steps
                        queue.append((dx, dy))
                        grid[dx][dy] = -1
            
            steps += 1
        
        return -1