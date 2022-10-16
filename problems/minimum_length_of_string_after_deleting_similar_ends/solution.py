class Solution:
    def minimumLength(self, s: str) -> int:
        d = collections.deque(s)
        
        while len(d) >= 2 and d[0] == d[-1]:
            current = d[0]
            
            while len(d) > 0 and d[0] == current:
                d.popleft()
            
            while len(d) > 0 and d[-1] == current:
                d.pop()
        
        return len(d)