class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        res = 0
        for (prevX,prevY), (currX,currY) in zip(points, points[1:]):
            res += max(abs(prevX-currX), abs(prevY-currY))
        
        return res