class Solution:
    def executeInstructions(self, n: int, startPos: List[int], s: str) -> List[int]:
        res = []
        m = len(s)
        
        for i in range(m):
            x, y = startPos
            count = 0
            
            for j in range(i, m):
                if s[j] == "R":
                    x, y = x, y + 1
                elif s[j] == 'L':
                    x, y = x, y - 1
                elif s[j] == 'U':
                    x, y = x - 1, y
                else:
                    x, y = x + 1, y
                    
                if 0 <= x < n and 0 <= y < n:
                    count += 1
                else:
                    break
            
            res.append(count)
        
        return res