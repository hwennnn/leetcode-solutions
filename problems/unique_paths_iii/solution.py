class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        available = 0
        sx = sy = ex = ey = 0
        res = 0
        
        for x in range(rows):
            for y in range(cols):
                if grid[x][y] != -1:
                    available += 1
                
                if grid[x][y] == 1:
                    sx, sy = x, y
                elif grid[x][y] == 2:
                    ex, ey = x, y
                    
        queue = deque([(sx, sy, 1, set([(sx, sy)]))])
        
        while queue:
            x, y, count, visited = queue.popleft()
            
            if x == ex and y == ey and count == available:
                res += 1
                continue
            
            for dx, dy in [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]:
                if 0 <= dx < rows and 0 <= dy < cols and grid[dx][dy] != -1 and count + 1 <= available and (dx, dy) not in visited:
                    new_visited = visited | {(dx, dy)}
                    queue.append((dx, dy, count + 1, new_visited))
        
        return res