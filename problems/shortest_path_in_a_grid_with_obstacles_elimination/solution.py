class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        rows, cols = len(grid), len(grid[0])
        queue = collections.deque([(0, 0, 0, k)])
        visited = set([(0, 0, k)])
        
        while queue:
            x, y, steps, skip = queue.popleft()

            if x == rows - 1 and y == cols - 1:
                return steps
            
            for dx, dy in [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]:
                if 0 <= dx < rows and 0 <= dy < cols:
                    if grid[dx][dy] == 0 and (dx, dy, skip) not in visited:
                        queue.append((dx, dy, steps + 1, skip))
                        visited.add((dx, dy, skip))
                    elif grid[dx][dy] == 1 and skip >= 1 and (dx, dy, skip - 1) not in visited:
                        queue.append((dx, dy, steps + 1, skip - 1))
                        visited.add((dx, dy, skip - 1))
            
        return -1