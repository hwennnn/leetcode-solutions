class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        fresh = mins = 0
        queue = collections.deque()
        
        for x in range(rows):
            for y in range(cols):
                if grid[x][y] == 2:
                    queue.append((x, y))
                    
                elif grid[x][y] == 1:
                    fresh += 1
                    
        if fresh == 0: return 0
        
        while queue:
            n = len(queue)
            
            for _ in range(n):
                x, y = queue.popleft()
                
                for dx, dy in [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]:
                    if 0 <= dx < rows and 0 <= dy < cols and grid[dx][dy] == 1:
                        grid[dx][dy] = 2
                        queue.append((dx, dy))
                        fresh -= 1
                        
            mins += 1
        
        return mins - 1 if fresh == 0 else -1