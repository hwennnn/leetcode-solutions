class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        rows, cols = len(grid), len(grid[0])
        
        queue = deque([(k, 0, 0, 0)])
        visited = set([(0, 0, k)])
        
        while queue:
            r, steps, x, y = queue.popleft()
            
            if x == rows - 1 and y == cols - 1:
                return steps
            
            for dx, dy in [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]:
                if 0 <= dx < rows and 0 <= dy < cols:
                    if r > 0 and grid[dx][dy] == 1 and (dx, dy, r - 1) not in visited:
                        queue.append((r - 1, steps + 1, dx, dy))
                        visited.add((dx, dy, r - 1))
                    elif grid[dx][dy] == 0 and (dx, dy, r) not in visited:
                        queue.append((r, steps + 1, dx, dy))
                        visited.add((dx, dy, r))
        
        return -1