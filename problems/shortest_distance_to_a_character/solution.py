class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        pos = deque([i for i,x in enumerate(s) if x == c])
        res = []
        prev = pos[0]
        
        for i,x in enumerate(s):
            
            if pos and pos[0] == i:
                prev = pos.popleft()
            
            if x == c:
                res.append(0)
            else:
                res.append(min(i - prev if i > prev else prev - i, pos[0] - i if pos else float('inf')))
        
        return res