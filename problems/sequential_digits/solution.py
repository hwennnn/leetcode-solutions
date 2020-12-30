class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        
        q = collections.deque(range(1,10))
        res = []
        
        while q:
            v = q.popleft()
            if low <= v <= high:
                res.append(v)
            
            last = v%10
            
            if last < 9:
                q.append(v*10 + last + 1)
        
        return res