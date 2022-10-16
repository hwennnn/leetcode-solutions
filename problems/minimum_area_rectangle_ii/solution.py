class Solution:
    def minAreaFreeRect(self, points: List[List[int]]) -> float:
        n = len(points)
        res = float('inf')
        pos = set([(x, y) for x, y in points])
        
        def distance(x1, y1, x2, y2):
            return (x2 - x1) ** 2 + (y2 - y1) ** 2
        
        for i in range(n):
            x1, y1 = points[i]
            for j in range(i + 1, n):
                x2, y2 = points[j]
                for k in range(j + 1, n):
                    x3, y3 = points[k]

                    if distance(x2, y2, x3, y3) + distance(x1, y1, x3, y3) != distance(x1, y1, x2, y2): continue
                    
                    x4 = x1 + x2 - x3
                    y4 = y1 + y2 - y3
                    
                    if (x4, y4) not in pos: continue
                    
                    area = math.sqrt(distance(x1, y1, x3, y3)) * math.sqrt(distance(x2, y2, x3, y3))
                    
                    if area == 0: continue
                    
                    res = min(res, area)
        
                
        return res if res != float('inf') else 0