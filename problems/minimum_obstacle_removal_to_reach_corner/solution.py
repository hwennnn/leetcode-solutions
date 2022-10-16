class Solution:
    def minimumObstacles(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        
        dp = [[float('inf')] * cols for _ in range(rows)]
        dp[0][0] = 0
        
        queue = deque([(0, 0, 0)])
        
        while queue:
            x, y, obs = queue.popleft()
            
            for dx, dy in [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]:
                if 0 <= dx < rows and 0 <= dy < cols:
                    old = dp[dx][dy]
                    new = obs + grid[dx][dy]
                    
                    if new < old:
                        dp[dx][dy] = new
                        if grid[dx][dy] == 1:
                            queue.append((dx, dy, new))
                        else:
                            queue.appendleft((dx, dy, new))
        
        return dp[-1][-1]