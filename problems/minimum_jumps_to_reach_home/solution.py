class Solution:
    def minimumJumps(self, forbidden: List[int], a: int, b: int, x: int) -> int:
        f = set(forbidden)
        
        queue = deque([(0, 0, False)])
        maxVal = max([x] + forbidden) + a + b
        visited = set([0])
        
        while queue:
            curr, steps, isBackward = queue.popleft()
            
            if curr == x:
                return steps
            
            forward = curr + a
            if forward <= maxVal and forward not in f and (forward, False) not in visited:
                visited.add((forward, False))
                queue.append((forward, steps + 1, False))
            
            backward = curr - b
            if not isBackward and backward >= 0 and backward not in f and (backward, True) not in visited:
                visited.add((backward, True))
                queue.append((backward, steps + 1, True))
        
        return -1