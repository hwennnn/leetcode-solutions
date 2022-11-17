class Solution:
    def computeArea(self, ax1: int, ay1: int, ax2: int, ay2: int, bx1: int, by1: int, bx2: int, by2: int) -> int:
        areaA = (ax2 - ax1) * (ay2 - ay1)
        areaB = (bx2 - bx1) * (by2 - by1)
        w = max(min(ax2, bx2) - max(ax1, bx1), 0)
        h = max(min(ay2, by2) - max(ay1, by1), 0)
        overlap = w * h
        
        return areaA + areaB - overlap