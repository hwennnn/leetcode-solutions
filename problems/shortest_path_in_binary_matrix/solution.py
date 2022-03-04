class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        if grid[0][0] == 1: return -1
        grid[0][0] = 1
        queue = deque([(0, 0, 1)])
        
        while queue:
            x, y, steps = queue.popleft()
            
            if x == rows - 1 and y == cols - 1:
                return steps
            
            for i in range(-1, 2):
                for j in range(-1, 2):
                    dx, dy = x + i, y + j
                    if 0 <= dx < rows and 0 <= dy < cols and grid[dx][dy] == 0:
                        grid[dx][dy] = 1
                        queue.append((dx, dy, steps + 1))
                    
        
        return -1