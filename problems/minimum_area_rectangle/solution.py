class Solution:
    def minAreaRect(self, points: List[List[int]]) -> int:
        n = len(points)
        p = defaultdict(set) 
        res = float('inf')
        
        for x, y in points:
            p[x].add(y)

        for i in range(n):
            x1, y1 = points[i]
            for j in range(i + 1, n):
                x2, y2 = points[j]
                if x1 == x2 or y1 == y2: continue
                
                # x3, y3 = x1, y2
                # x4, y4 = x2, y1
                
                if y2 in p[x1] and y1 in p[x2]:
                    area = abs(x2 - x1) * abs(y1 - y2)
                    res = min(res, area)
                        
        return 0 if res == float('inf') else res