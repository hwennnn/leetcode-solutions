class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        res = right = 0
        
        intervals.sort(key = lambda x:(x[0],-x[1]))
        
        for start,end in intervals:
            res += end > right
            right = max(right, end)
        
        return res