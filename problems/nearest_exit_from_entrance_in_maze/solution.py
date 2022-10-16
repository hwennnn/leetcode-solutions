class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        rows, cols = len(maze), len(maze[0])
        sx, sy = entrance
        queue = deque([(sx, sy, 0)])
        maze[sx][sy] = "+"
        
        while queue:
            x, y, steps = queue.popleft()
            
            if (x, y) != (sx, sy) and (x == 0 or x == rows - 1 or y == 0 or y == cols - 1): return steps
            
            for dx, dy in [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]:
                if 0 <= dx < rows and 0 <= dy < cols and maze[dx][dy] == ".":
                    maze[dx][dy] = "+"
                    queue.append((dx, dy, steps + 1))
        
        return -1