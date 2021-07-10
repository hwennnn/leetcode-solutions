class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        rows, cols = len(maze), len(maze[0])
        ox, oy = entrance
        if maze[ox][oy] == '+': return -1
        
        queue = collections.deque([[ox, oy, 0]])
        visited = set([(ox, oy)])
        
        while queue:
            x, y, steps = queue.popleft()
            if steps > 0 and (x == 0 or y == 0 or x == rows - 1 or y == cols - 1): return steps
            
            for dx, dy in ((x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)):
                if 0 <= dx < rows and 0 <= dy < cols and (dx, dy) not in visited and maze[dx][dy] == '.':
                    visited.add((dx, dy))
                    queue.append((dx, dy, steps + 1))
        
        return -1