class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        N = len(intervals)
        sx, sy = newInterval
        left, right = [], []

        for x, y in intervals:
            if y < sx:
                left.append([x, y])
            elif x > sy:
                right.append([x, y])
            else:
                sx = min(sx, x)
                sy = max(sy, y)
        
        return left + [[sx, sy]] + right