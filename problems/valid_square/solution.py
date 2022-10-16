class Solution:
    def validSquare(self, p1: List[int], p2: List[int], p3: List[int], p4: List[int]) -> bool:
        points = [p1,p2,p3,p4]
        
        def dist(a, b):
            return (a[0] - b[0])**2 + (a[1] - b[1])**2
        
        res = []
        
        for i in range(4):
            for j in range(i+1, 4):
                res.append(dist(points[i], points[j]))
        
        res.sort()
        
        return res[0] > 0 and res[0] == res[1] and res[0] == res[2] and res[0] == res[3] and res[4] == res[5]