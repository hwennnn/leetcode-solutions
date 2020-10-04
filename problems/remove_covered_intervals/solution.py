class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda a: (a[0], -a[1]))
        res = right = 0
        
        for x,y in intervals:
            res += y > right
            right = max(right, y)

        return res