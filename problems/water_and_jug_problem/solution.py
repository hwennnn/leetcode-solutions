class Solution:
    def canMeasureWater(self, x: int, y: int, z: int) -> bool:
        if x + y < z: return False
        
        queue = deque([(0, 0)])
        visited = set([(0, 0)])
        
        while queue:
            a, b = queue.popleft()
            
            if a + b == z: return True
            
            states = set()
            
            states.add((x, b))
            states.add((a, y))
            states.add((0, b))
            states.add((a, 0))
            states.add((min(x, a + b), b - (x - a) if b - (x - a) > 0 else 0))
            states.add((a - (y - b) if a - (y - b) > 0 else 0, min(y, b + a)))
            
            for state in states:
                if state not in visited:
                    visited.add(state)
                    queue.append(state)
            
        
        return False
        