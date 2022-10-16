class Solution:
    def countGoodRectangles(self, rectangles: List[List[int]]) -> int:
        res = []
        
        for a,b in rectangles:
            res.append(min(a,b))
        
        return res.count(max(res))