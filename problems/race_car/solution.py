class Solution:
    def racecar(self, target: int) -> int:
        queue = deque([(0, 1, 0)])
        visited = set([(0, 1)])
        
        while queue:
            x, speed, steps = queue.popleft()
            
            if x == target: return steps
            
            A = [(x + speed, speed * 2, steps + 1), (x, -1 if speed > 0 else 1, steps + 1)]
            
            for y, newSpeed, newSteps in A:
                if 0 < y < target * 2 and (y, newSpeed) not in visited:
                    queue.append((y, newSpeed, newSteps))
                    visited.add((y, newSpeed))
                    
        return -1