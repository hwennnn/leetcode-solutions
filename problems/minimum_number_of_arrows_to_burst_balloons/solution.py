class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        n = len(points)
        points.sort(key = lambda x : x[1])
        shoot = points[0][1]
        res = 1
        
        for i in range(1, n):
            
            if points[i][0] > shoot:
                res += 1
                shoot = points[i][1]
        
        return res
        