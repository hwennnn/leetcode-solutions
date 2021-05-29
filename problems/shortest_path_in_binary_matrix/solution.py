class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        if grid[0][0] == 1: return -1
        
        queue = collections.deque([(0, 0, 1)])
        visited = set()
        
        while queue:
            x, y, steps = queue.popleft()
            if x == rows - 1 and y == cols - 1: return steps
            
            for dx in range(x - 1, x + 2):
                for dy in range(y - 1, y + 2):
                    if 0 <= dx < rows and 0 <= dy < cols and grid[dx][dy] == 0 and (dx, dy) not in visited:
                        queue.append((dx, dy, steps + 1))
                        visited.add((dx, dy))
        
        return -1