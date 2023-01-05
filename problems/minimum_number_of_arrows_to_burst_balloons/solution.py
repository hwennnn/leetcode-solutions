class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        N = len(points)
        points.sort(key = lambda x : x[1])
        shoot = points[0][1]
        res = 1
        
        for i in range(1, N):
            if points[i][0] > shoot:
                res += 1
                shoot = points[i][1]
        
        return res
        