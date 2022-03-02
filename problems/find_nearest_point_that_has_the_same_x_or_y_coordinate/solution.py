class Solution:
    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:
        res = -1
        distance = float('inf')
        
        for index, (x2, y2) in enumerate(points):
            if x2 == x or y2 == y:
                d = abs(x2 - x) + abs(y2 - y)
                if d < distance:
                    distance = d
                    res = index
        
        return res if distance != float('inf') else -1