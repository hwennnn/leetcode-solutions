class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        if not points: return 0
        
        points.sort(key = lambda x : (x[0], x[1]))
        
        res = 0
        prevX = points[0][0]
        for x,y in points[1:]:
            if x == prevX:
                continue
            else:
                res = max(res, x - prevX)
            prevX = x
        
        return res