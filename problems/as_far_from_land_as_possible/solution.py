class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        q = collections.deque()
        
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    for dx, dy in ((i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)):
                        q.append((dx, dy))
        
        steps = 0
        while q:
            steps += 1
            n = len(q)
            
            for _ in range(n):
                i, j = q.popleft()
                if 0 <= i < rows and 0 <= j < cols and grid[i][j] == 0:
                    grid[i][j] = steps
                    
                    for dx, dy in ((i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)):
                        q.append((dx, dy))
        
        return steps - 1 if steps != 1 else -1
        