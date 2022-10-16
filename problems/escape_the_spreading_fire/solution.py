class Solution:
    def maximumMinutes(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        INF = 10 ** 10
        dist = [[INF] * cols for _ in range(rows)]
        fire = deque()
        
        for x in range(rows):
            for y in range(cols):
                if grid[x][y] == 1:
                    dist[x][y] = 0
                    fire.append((0, x, y))
        
        while fire:
            d, x, y = fire.popleft()

            for dx, dy in [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]:
                if 0 <= dx < rows and 0 <= dy < cols and grid[dx][dy] != 2 and dist[dx][dy] == INF:
                    dist[dx][dy] = d + 1
                    fire.append((d + 1, dx, dy))
        
        def good(k):
            if dist[0][0] <= k: return False
            
            queue = deque([(k, 0, 0)])
            visited = [[False] * cols for _ in range(rows)]

            while queue:
                d, x, y = queue.popleft()

                for dx, dy in [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]:
                    if 0 <= dx < rows and 0 <= dy < cols and grid[dx][dy] != 2 and not visited[dx][dy] and d + 1 < dist[dx][dy]:
                        visited[dx][dy] = True
                        queue.append((d + 1, dx, dy))
                        
                        if dx == rows - 1 and dy == cols - 1: 
                            return True
                    
                    if dx == rows - 1 and dy == cols - 1 and grid[dx][dy] != 2 and not visited[dx][dy] and d + 1 <= dist[dx][dy]: 
                        return True

            
            return False

        left, right = 0, 10 ** 9
        
        while left < right:
            mid = (left + right + 1) // 2

            if good(mid):
                left = mid
            else:
                right = mid - 1
        
        if left == 0:
            return 0 if good(0) else -1
                
        return left
