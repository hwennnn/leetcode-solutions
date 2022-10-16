class Solution:
    def countPoints(self, points: List[List[int]], queries: List[List[int]]) -> List[int]:
        res = []
        
        for x, y, r in queries:
            count = 0
            
            for p1,p2 in points:
                dx = abs(p1 - x)
                dy = abs(p2 - y)
                
                count += int(dx**2 + dy**2 <= r**2)
            
            res.append(count)
        
        return res