class Solution:
    def minimumJumps(self, forbidden: List[int], a: int, b: int, x: int) -> int:
        
        visited = set()
        f = set(forbidden)
        max_val = max([x]+forbidden) + a + b
        deque = collections.deque([(0,0,0)])
        
        while deque:
            now, count, isBackward = deque.popleft()
            
            if now == x: return count
            
            if now + a not in f and now + a <= max_val and (now+a, False) not in visited:
                visited.add((now+a, False))
                deque.append((now+a, count+1, False))
            
            if now - b not in f and now - b >= 0 and not isBackward and (now-b, False) not in visited:
                visited.add((now-b, True))
                deque.append((now-b, count+1, True))
        
        return -1
                